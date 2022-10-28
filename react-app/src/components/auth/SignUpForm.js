import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [firstname, setFirstname] = useState('');
  const [lastname, setLastname] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password) {
      const data = await dispatch(signUp(firstname, lastname, email, password));
      if (data) {
        setErrors([data])
      }
    }
  };

  const updateFirstname = (e) => {
    setFirstname(e.target.value);
  };

  const updateLastname = (e) => {
    setLastname(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };


  if (user) {
    return <Redirect to='/designs' />;
  }

  return (
    <form onSubmit={onSignUp}>
      <h1>Log in or sign up in seconds</h1>
      <p>Use your email or login as a demo user to continue with Slate (it's free!)</p>
      <button
        id='demo-user'
        onClick={(e) => {
          updateEmail('periwinkle@user.io')
          updatePassword('password')
        }}
      >
        Continue with Demo User
      </button>
      <div>
      <div id='form-input-1'>
        <div>
        <label>First Name</label>
        <input
          type='text'
          name='firstname'
          placeholder='First name'
          onChange={updateFirstname}
          value={firstname}
        ></input>
        </div>
        <div>
        <label>Last Name</label>
        <input
          type='text'
          name='lastname'
          placeholder='Last name'
          onChange={updateLastname}
          value={lastname}
          required={true}
        ></input>
        </div>
      </div>
      </div>
      <div id='form-input'>
        <label>Email</label>
        <input
          type='email'
          name='email'
          placeholder='user@example.io'
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div id='form-input'>
        <label>Password</label>
        <input
          type='password'
          name='password'
          placeholder='Enter password'
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <button id='login-submit' type='submit'>Sign Up</button>
    </form>
  );
};

export default SignUpForm;
