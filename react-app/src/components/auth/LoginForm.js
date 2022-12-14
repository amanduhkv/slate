import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';




const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [submitted, setSubmitted] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();

    setSubmitted(true);

    const data = await dispatch(login(email, password));
    if (data) {
      // console.log(data)
      setErrors(['Invalid credentials. Please check your email/password.']);
    }
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
    <form onSubmit={onLogin}>
      <h1>Log in or sign up in seconds</h1>
      <p>Use your email or login as a demo user to continue with Slate (it's free!)</p>
      <button
        id='demo-user'
        onClick={() => {
          setEmail('periwinkle@user.io')
          setPassword('password')
        }}
      >
        Continue with Demo User
      </button>
      {submitted && errors.length > 0 && (
        <div className='errors'>
          {errors.map((error, ind) => (
            <div key={ind}>{error}</div>
          ))}
        </div>
      )}
      <div id='form-input'>
        <label htmlFor='email'>Email</label>
        <input
          name='email'
          placeholder='user@example.io'
          type='text'
          value={email}
          onChange={updateEmail}
          onKeyPress={e => e.key === 'Enter' && e.preventDefault()}
        />
        {/* <div id='login-err'>
          {errors.map((error) => error.toLowerCase().includes('email') ? error : null)}
        </div> */}
      </div>
      <div id='form-input'>
        <label htmlFor='password'>Password</label>
        <input
          name='password'
          placeholder='Enter password'
          type='password'
          value={password}
          onChange={updatePassword}
          onKeyPress={e => e.key === 'Enter' && e.preventDefault()}
        />
        {/* <div id='login-err'>
          {errors.map((error) => error.toLowerCase().includes('password') ? error : null)}
        </div> */}
      </div>
      <button
        id='login-submit'
        type='submit'
        // onKeyPress={e => e.key === 'Enter' && e.preventDefault()}
      >
        Log in
      </button>
    </form>
  );
};

export default LoginForm;
