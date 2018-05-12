import {MDCRipple, MDCRippleFoundation, util} from '@material/ripple';
import {Vue, Vuex, VueResurse} from './vue.js'

import header from './blocks/header/header';
import sideMenu from './blocks/side-menu/side-menu';
import navMenu from './blocks/nav-menu/nav-menu';

const surfaces = document.getElementsByClassName('ripple')

for (let i=0; i < surfaces.length; i++) {
    MDCRipple.attachTo(surfaces[i]);
}

