import React, { Component, Suspense } from 'react';
import { Route, Redirect, Switch } from 'react-router-dom';

import BardScreen from 'screens/BardScreen/BardScreen';

import './Router.scss';



class Router extends Component {

  componentDidMount(){
  }

  componentDidUpdate() {
  }

  render() {
    return (
      <>
        <Suspense >
          <Switch>
            <Route path="/" exact component={BardScreen} />
          </Switch>
        </Suspense>
      </>
    );
  }
}

export default Router;
