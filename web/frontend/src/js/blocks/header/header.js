import { Vue } from '../../vue.js';

import store from '../../store'


var header = new Vue({
    name: 'header',
    el: '#js-header',
    store,
    data: {
        sideMenuIsActive: false,
    },
    mounted: function () {

    },
    methods: {
        showSideMenu: function () {
            this.$store.commit("showSideMenu/show");
        },
        hideSideMenu: function () {
            this.$store.commit("showSideMenu/hide");
        },
        test: function () {
            this.sideMenuIsActive = false;
        },
    }
})

var headerBottom = document.getElementById('header-bottom');
var stuck = false;
var stickPoint = getDistance();

function getDistance () {
    let topDist = headerBottom.offsetTop;
    return topDist;
}

// window.onscroll = function (e) {
//     let offset = window.pageYOffset;
//     let distance = getDistance() - offset;
//     if ( (distance <= 0) && !stuck ) {
//         stuck = true;
//         headerBottom.style.position = 'fixed';
//         headerBottom.style.top = '100px';
//         console.log('stucked');
//     } else if ( stuck && (offset <= stickPoint) ) {
//         stuck = false;
//         headerBottom.style.position = 'static';
//         console.log('unstucked');
//     }
// }

