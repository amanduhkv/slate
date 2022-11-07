import React, { useState, useEffect } from 'react';
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { authenticate } from './store/session';

import LoginPage from './components/auth/LoginPage/LoginPage';

import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';

import Designs from './components/Designs';
import UserDesigns from './components/Designs/UserDesigns';
import SingleDesign from './components/Designs/SingleDesign';
import CreateDesign from './components/CreateDesignForm';
import Brands from './components/Brands';
import UserBrands from './components/Brands/UserBrands';
import SingleBrand from './components/Brands/SingleBrand';
import CreateBrand from './components/CreateBrandForm/CreateBrand';
import UpdateBrand from './components/Brands/UpdateBrand';
import ErrPage from './components/Err';

function App() {
  const user = useSelector(state => state.session.user);
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Switch>
        <ProtectedRoute path='/' exact={true} >
          {user && (
            <Redirect to='/designs' />
          )}
          {!user && (
            <Redirect to='/login' />
          )}
        </ProtectedRoute>
        <Route path='/login' exact={true}>
          <LoginPage />
        </Route>
        <Route path='/signup' exact={true}>
          <LoginPage />
        </Route>
        {/* <ProtectedRoute path='/users' exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
         */}
        <Route path='/designs/current' exact={true}>
          <NavBar />
          <UserDesigns />
        </Route>
        <Route path='/designs/new'>
          {/* <NavBar /> */}
          <CreateDesign />
        </Route>
        <Route path='/designs/:designId' >
          {/* <NavBar /> */}
          <SingleDesign />
        </Route>
        <Route path='/designs' exact={true}>
          <Designs />
        </Route>

        {/* <Route path='/brand/current' exact={true}>
          <NavBar />
          <UserBrands />
        </Route> */}
        <Route path='/brand/current'>
          <ErrPage />
        </Route>
        <Route path='/brand/new' exact={true}>
          <NavBar />
          <CreateBrand />
        </Route>
        <Route path='/brand/:brandId/edit' exact={true}>
          <NavBar />
          <UpdateBrand />
        </Route>
        <Route path='/brand/:brandId' exact={true}>
          <NavBar />
          <SingleBrand />
        </Route>
        <Route path='/brand' exact={true}>
          <NavBar />
          <Brands />
        </Route>

      </Switch>
    </BrowserRouter>
  );
}

export default App;
