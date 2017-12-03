
export default {
    namespaced: true,
    state: function(){
        return {
            isVisible: false
        }
    },
    mutations: {
        show(state) {
            state.isVisible = true;
        },
        hide(state) {
            state.isVisible = false;
        },
        toggle(state) {
            state.isVisible = !state.isVisible;
        }
    }
};