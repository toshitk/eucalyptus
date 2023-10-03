import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import '@mdi/font/css/materialdesignicons.css'
import { RouteLocationRaw } from 'vue-router'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/styles'
import { clientId, domain } from "../authConfig.json"
import { Auth0Plugin } from "./auth"

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App).use(vuetify).use(Auth0Plugin, {
  domain,
  clientId,
  onRedirectCallback: (appState: { targetUrl: RouteLocationRaw }) => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

app.mount('#app')
