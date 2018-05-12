import { Vue } from '../../vue.js';
import { setTimeout } from 'timers';

import store from '../../store'


var navMenu = new Vue({
    name: 'nav-menu',
    el: '#nav-menu',
    store,
    data: {
        isActive: false
    },
    computed: {
        isVisible() {
            return this.$store.state.showNavMenu.isVisible;
        }
    },
    methods: {
        hideNavMenu() {
            document.body.style.overflow='auto';
            this.$store.commit("showNavMenu/hide");
        }
    },
    watch: {
        isVisible: function () {
            let navMenuSelector = document.getElementById('nav-menu');
            if ( this.isVisible ) {
                document.body.style.overflow='hidden';
                navMenuSelector.style.transform = 'translate3d(0,-100%,0)';
            } else {
                navMenuSelector.style.transform = 'none';
                setTimeout(function () {
                    document.body.style.overflow='auto';
                }, 300)
            }
        }
    }
})