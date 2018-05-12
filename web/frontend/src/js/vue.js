// Сторонние библиотеки
import Vue from 'vue';
import VueResource from 'vue-resource';
import Vuex from 'vuex';

// Конфигурирование

// Вшивание CSRF-токена в запросы vue-resurs
import csrfToken from './core/csrfToken';

Vue.use(VueResource);
Vue.use(Vuex);

Vue.http.headers.common['X-CSRFToken'] = csrfToken();

export {
    Vue,
    VueResource,
    Vuex,
}