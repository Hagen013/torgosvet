import { Vue } from '../../vue.js';
import { setTimeout } from 'timers';

import store from '../../store'


var sideMenu = new Vue({
    name: 'side-menu',
    el: '#side-menu',
    store,
    computed: {
        isVisible() {
            return this.$store.state.showSideMenu.isVisible;
        }
    },
    methods: {
        hideSideMenu() {
            this.$store.commit("showSideMenu/hide");
        },
        showNavMenu() {
            this.$store.commit("showSideMenu/hide");
            this.$store.commit("showNavMenu/show");
        }
    },
    watch: {
        isVisible: function() {
            let sideBar = document.getElementById('side-menu');
            let main = document.getElementById('main');
            let sideMenuContent = document.getElementById('side-menu__content');

            if ( this.isVisible ) {
                document.body.style.overflow='hidden';
                sideBar.style.visibility = "visible";
                main.style.transform = 'translate3d(-80%,0,0)';
                sideMenuContent.style.transform = 'translate3d(-80%,0,0)';
            } else {
                setTimeout(function () {
                    sideBar.style.visibility = "hidden";
                },300)
                main.style.transform = 'none';
                sideMenuContent.style.transform = 'none';
                document.body.style.overflow='auto';
            }
        }
    }
})