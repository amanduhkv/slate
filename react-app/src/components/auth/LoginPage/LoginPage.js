import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';
import { Modal } from '../../../context/Modal';
import { login } from '../../../store/session';

import backgd from '../../../icons/login-bckgd.svg'
import slate from '../../../icons/slate-white.png';
import './LoginPage.css';
import LoginForm from '../LoginForm';
import SignUpForm from '../SignUpForm';

const LoginPage = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showLogModal, setShowLogModal] = useState(true);
  const [showSignModal, setShowSignModal] = useState(false);

  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const history = useHistory();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <div id='img-bckgd' style={{ backgroundImage: `url(${backgd})` }}>
      <div className='login-page'>
        <div id='empty-div'></div>
        <div id='logo'>
          <img src={slate} alt='title' width='80px' />
          <span id='login-text'>
            Design spotlight
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#FFF" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
          </span>
          <span id='login-text'>
            Business
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#FFF" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
          </span>
          <span id='login-text'>
            Marketing
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#FFF" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
          </span>
          <span id='login-text'>
            Social Media
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#FFF" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
          </span>
        </div>
        <div>
          <button
            id='login-button'
            onClick={() => {
              setShowLogModal(true)
              setShowSignModal(false)
              history.replace({pathname: '/login'})
            }}
          >
            Log in
          </button>
          <button
            id='signup-button'
            onClick={() => {
              setShowSignModal(true)
              setShowLogModal(false)
              history.replace({pathname: '/signup'})
            }}
          >
            Sign up
          </button>
        </div>
        {showLogModal && (
          <Modal onClose={() => setShowLogModal(false)}>
            <LoginForm />
          </Modal>
        )}
        {showSignModal && (
          <Modal onClose={() => setShowSignModal(false)}>
            <SignUpForm />
          </Modal>
        )}
      </div>
    </div>
  );
};

export default LoginPage;
