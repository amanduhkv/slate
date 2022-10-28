import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import backgd from '../../icons/login-bckgd.svg'
import slate from '../../icons/slate-white.png';


const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      // console.log(data)
      setErrors([data.credential ?? data.password]);
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
    <form onSubmit={onLogin}>
      <h1>Log in or sign up in seconds</h1>
      <p>Use your email or login as a demo user to continue with Slate (it's free!)</p>
      <button
        id='demo-user'
      >
        Continue with Demo User
      </button>
      {/* <div>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div> */}
      <div id='form-input'>
        <label htmlFor='email'>Email</label>
        <input
          name='email'
          placeholder='user@example.io'
          type='text'
          value={email}
          onChange={updateEmail}
        />
        <div id='login-err'>
          {errors.map((error) => error.toLowerCase().includes('email') ? error : null)}
        </div>
      </div>
      <div id='form-input'>
        <label htmlFor='password'>Password</label>
        <input
          name='password'
          placeholder='Enter password'
          type='password'
          value={password}
          onChange={updatePassword}
        />
        <div id='login-err'>
          {errors.map((error) => error.toLowerCase().includes('password') ? error : null)}
        </div>
      </div>
        <button id='login-submit' type='submit'>Log in</button>
        <p>By continuing, you agree to Slate's Terms of Use, and realize this is simply a clone.</p>
        <button
          id='login-signup-button'
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M20.37 5.03A2 2 0 0 1 22 7v10a2 2 0 0 1-1.96 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h16.1H4zm.13 2.07-4.53 5.31 4.53 4.63a.5.5 0 0 0 0-.04V7.1zm-17-.14a.5.5 0 0 0 0 .04v10a.5.5 0 0 0 0 .04l4.59-4.7L3.5 6.97zm5.57 6.53-3.92 4 13.7.01L15 13.56a4 4 0 0 1-5.93-.07zm9.88-6.99H5l5.07 5.96a2.5 2.5 0 0 0 3.81 0l5.07-5.96z"></path></svg>
          Sign up with your email
        </button>
    </form>
  );
};

export default LoginForm;
