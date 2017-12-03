import {Vuex} from '../vue.js';

import showModal from './modules/show-modal.js';


export default new Vuex.Store({
    modules: {
        showSideMenu: showModal,
        showNavMenu: showModal
    },
    actions:{

    }
})