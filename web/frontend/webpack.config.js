const webpack = require("webpack");
const path = require("path");
//const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  context: path.resolve(__dirname, "./src/js"),

  entry: {
    scripts: './scripts.js',
    index: './index.js'
  },
  output: {
    path: path.resolve(__dirname, "./static/js"),
    publicPath: "/static/js/",
    filename: "[name].js"
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: "vue-loader",
        options: {
          loaders: {
            scss: "vue-style-loader!css-loader!sass-loader",
            sass: "vue-style-loader!css-loader!sass-loader?indentedSyntax",
            js: 'babel-loader?presets[]=es2015,presets[]=es2016'
          }
        }
      },
      {
        test: /\.js$/,
        loader: "babel-loader",
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'es2016']
        }
      }
    ]
  },
  resolve: {
    modules: [path.resolve(__dirname, "./src"), "node_modules"],
    alias: {
      vue$: "vue/dist/vue.common.js"
      //vue$: 'vue/dist/vue.esm.js'
    }
  },
  devtool: 'source-map',
  devServer: {
    publicPath: "/static/js/",
    disableHostCheck: true,
    // contentBase: path.resolve(__dirname, "./static/js"), //__dirname + '/frontend/',
    proxy: {
      "/": "http://localhost:8000"
    }
  },
};

module.exports.plugins = (module.exports.plugins || []).concat([

  new webpack.optimize.CommonsChunkPlugin({
    name: 'common',
    filename: 'common.js'
  }),

]);

if (process.env.NODE_ENV === "production") {
  module.exports.devtool = false;

  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      "process.env.NODE_ENV": '"production"'
    }),

    // new webpack.optimize.UglifyJsPlugin({
    //   comments: false
    //   //except: ['$super', '$', 'exports', 'require', 'self', 'STORE']
    //   //compress: { warnings: false }
    // }),

    new webpack.optimize.CommonsChunkPlugin({
      name: 'common',
      filename: 'common.js'
    }),

    new webpack.LoaderOptionsPlugin({
      //minimize: true
    })
  ]);
}