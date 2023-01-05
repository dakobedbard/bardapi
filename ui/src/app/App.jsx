import { Provider } from "react-redux";
import Router from './Router';
import { BrowserRouter, Route } from 'react-router-dom';

import store from './store'
// import store from './store'
import TodoApp from '../TodoApp'

function App() {
  // extends blueprint icon renderer to render icons from the ftm iconRegistry

  return (
    <Provider store={store}>
      <TodoApp />
      <BrowserRouter>
        <Route path="/" component={Router} />
      </BrowserRouter>
    
    </Provider>

  );
}


export default App;