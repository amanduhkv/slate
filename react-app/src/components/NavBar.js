import React from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css';

import slate from '../icons/slate.png';
import avi from '../icons/avi.svg';
import LoginForm from './auth/LoginForm';

const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user);


  return (
    <nav>
      <div className='left-nav'>

        <div id='hamburger'>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5.75 5.25h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 0 1 0-1.5zm0 6h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 1 1 0-1.5zm0 6h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 1 1 0-1.5z"></path></svg>
        </div>

        <div
          className='logo'
          onClick={() => window.location = '/designs'}
        >
          <img src={slate} width='80px' />
        </div>

        <button id='nav-title-buttons'>
          Design spotlight
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#484C4F" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
        </button>
        <button id='nav-title-buttons'>
          Business
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#484C4F" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
        </button>
        <button id='nav-title-buttons'>
          Marketing
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#484C4F" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
        </button>
        <button id='nav-title-buttons'>
          Social Media
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#484C4F" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
        </button>
      </div>

      <div className='right-nav'>
        <button
          onClick={() => window.location = '/designs/new'}
        >
          Create a design
        </button>
        <div id='user-initial'>
          {sessionUser ? sessionUser.firstname[0] : <img src={avi} height='20px' />}
        </div>
        {/* <LogoutButton /> */}
      </div>
    </nav>
  );
}

export default NavBar;
