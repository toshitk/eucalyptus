import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { createAuth0 } from '@auth0/auth0-vue'
import '@mdi/font/css/materialdesignicons.css'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/styles'
// import { clientId, domain } from "../authConfig.json"
// import { Auth0Plugin } from "./auth"

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App).use(vuetify).use(router).use(createAuth0({
    domain: "dev-e3ybvpddsjl3sbd7.us.auth0.com",
    clientId: "Q4cCWeXXVl79APpfoT8WP1k7zygYDKJy",
    authorizationParams: {
      redirect_uri: window.location.origin
    }
  })
);

app.mount('#app')
