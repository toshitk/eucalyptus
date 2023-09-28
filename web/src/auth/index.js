import { createAuth0Client } from "@auth0/auth0-spa-js";
import { reactive } from 'vue';

/** Define a default action to perform after authentication */
const DEFAULT_REDIRECT_CALLBACK = () =>
  window.history.replaceState({}, document.title, window.location.pathname);

let instance;

/** Returns the current instance of the SDK */
export const getInstance = () => instance;

/** Creates an instance of the Auth0 SDK. If one has already been created, it returns that instance */
export const useAuth0 = ({
  onRedirectCallback = DEFAULT_REDIRECT_CALLBACK,
  redirectUri = window.location.origin,
  ...options
}) => {
  if (instance) return instance;

  const state = reactive({
    loading: true,
    isAuthenticated: false,
    user: {},
    auth0Client: null,
    popupOpen: false,
    error: null
  });

  const loginWithPopup = async (options, config) => {
    state.popupOpen = true;

    try {
      await state.auth0Client.loginWithPopup(options, config);
      state.user = await state.auth0Client.getUser();
      state.isAuthenticated = await state.auth0Client.isAuthenticated();
      state.error = null;
    } catch (e) {
      state.error = e;
      console.error(e);
    } finally {
      state.popupOpen = false;
    }

    state.user = await state.auth0Client.getUser();
    state.isAuthenticated = true;
  };

  const handleRedirectCallback = async () => {
    state.loading = true;
    try {
      await state.auth0Client.handleRedirectCallback();
      state.user = await state.auth0Client.getUser();
      state.isAuthenticated = true;
      state.error = null;
    } catch (e) {
      state.error = e;
    } finally {
      state.loading = false;
    }
  };

  const loginWithRedirect = o => {
    return state.auth0Client.loginWithRedirect(o);
  };

  const getIdTokenClaims = o => {
    return state.auth0Client.getIdTokenClaims(o);
  };

  const getTokenSilently = o => {
    return state.auth0Client.getTokenSilently(o);
  };

  const getTokenWithPopup = o => {
    return state.auth0Client.getTokenWithPopup(o);
  };

  const logout = o => {
    return state.auth0Client.logout(o);
  };

  const created = async () => {
    state.auth0Client = await createAuth0Client({
      ...options,
      client_id: options.clientId,
      redirect_uri: redirectUri
    });

    try {
      if (
        window.location.search.includes("code=") &&
        window.location.search.includes("state=")
      ) {
        const { appState } = await state.auth0Client.handleRedirectCallback();
        state.error = null;
        onRedirectCallback(appState);
      }
    } catch (e) {
      state.error = e;
    } finally {
      state.isAuthenticated = await state.auth0Client.isAuthenticated();
      state.user = await state.auth0Client.getUser();
      state.loading = false;
    }
  };

  created();

  instance = {
    ...state,
    loginWithPopup,
    handleRedirectCallback,
    loginWithRedirect,
    getIdTokenClaims,
    getTokenSilently,
    getTokenWithPopup,
    logout
  };

  return instance;
};

// Create a simple Vue plugin to expose the wrapper object throughout the application
export const Auth0Plugin = {
  install(app, options) {
    app.config.globalProperties.$auth = useAuth0(options);
  }
};
