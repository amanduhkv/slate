import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, useHistory, useLocation } from 'react-router-dom';
import { Modal } from '../../../context/Modal';
import { login } from '../../../store/session';

import backgd from '../../../icons/login-bckgd.png'
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
  const url = useLocation().pathname;

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
              window.history.pushState({}, '', '/login')
            }}
          >
            Log in
          </button>
          <button
            id='signup-button'
            onClick={() => {
              setShowSignModal(true)
              setShowLogModal(false)
              window.history.pushState({}, '', '/signup')
            }}
          >
            Sign up
          </button>
        </div>
        {showLogModal && (
          <Modal onClose={() => setShowLogModal(false)}>
            <LoginForm />
            <p>By continuing, you agree to Slate's Terms of Use, and realize this is simply a clone.</p>
            <button
              id='login-signup-button'
              onClick={() => {
                setShowLogModal(false)
                setShowSignModal(true)
              }}
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M20.37 5.03A2 2 0 0 1 22 7v10a2 2 0 0 1-1.96 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h16.1H4zm.13 2.07-4.53 5.31 4.53 4.63a.5.5 0 0 0 0-.04V7.1zm-17-.14a.5.5 0 0 0 0 .04v10a.5.5 0 0 0 0 .04l4.59-4.7L3.5 6.97zm5.57 6.53-3.92 4 13.7.01L15 13.56a4 4 0 0 1-5.93-.07zm9.88-6.99H5l5.07 5.96a2.5 2.5 0 0 0 3.81 0l5.07-5.96z"></path></svg>
              Sign up with your email
            </button>
          </Modal>
        )}
        {showSignModal && (
          <Modal onClose={() => setShowSignModal(false)}>
            <SignUpForm />
            <p>By continuing, you agree to Slate's Terms of Use, and realize this is simply a clone.</p>
            <button
              id='login-signup-button'
              onClick={() => {
                setShowLogModal(true)
                setShowSignModal(false)
              }}
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M20.37 5.03A2 2 0 0 1 22 7v10a2 2 0 0 1-1.96 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h16.1H4zm.13 2.07-4.53 5.31 4.53 4.63a.5.5 0 0 0 0-.04V7.1zm-17-.14a.5.5 0 0 0 0 .04v10a.5.5 0 0 0 0 .04l4.59-4.7L3.5 6.97zm5.57 6.53-3.92 4 13.7.01L15 13.56a4 4 0 0 1-5.93-.07zm9.88-6.99H5l5.07 5.96a2.5 2.5 0 0 0 3.81 0l5.07-5.96z"></path></svg>
              Log in with your email
            </button>
          </Modal>
        )}
      </div>
    </div>
  );
};

export default LoginPage;
