import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css';

import slate from '../icons/slate.png';
import avi from '../icons/avi.svg';
import LoginForm from './auth/LoginForm';
import Designs from './Designs';

const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user);

  const [showProfMenu, setShowProfMenu] = useState(false);
  const [showHamMenu, setShowHamMenu] = useState(false);
  const [showDesMenu, setShowDesMenu] = useState(false);
  const history = useHistory();

  // OPEN/CLOSE MENU FXNS ---------------------------------------------------
  const openProfMenu = () => {
    if (showProfMenu) return;
    setShowProfMenu(true);
  };
  const openHamMenu = () => {
    if (showHamMenu) return;
    setShowHamMenu(true);
  };
  const openDesMenu = () => {
    if (showDesMenu) return;
    setShowDesMenu(true);
  };
  const closeDesMenu = () => {
    setShowDesMenu(false);
  };
  // MENU USE-EFFECTS -------------------------------------------------
  useEffect(() => {
    if (!showProfMenu) return;
    const closeProfMenu = () => {
      setShowProfMenu(false);
    };
    document.addEventListener('click', closeProfMenu);
    return () => document.removeEventListener("click", closeProfMenu);
  }, [showProfMenu]);

  useEffect(() => {
    if (!showHamMenu) return;
    const closeHamMenu = () => {
      setShowHamMenu(false);
    };
    document.addEventListener('click', closeHamMenu);
    return () => document.removeEventListener("click", closeHamMenu);
  }, [showHamMenu]);


  return (
    <nav>
      <div className='left-nav'>

        <div id='hamburger' onClick={openHamMenu}>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5.75 5.25h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 0 1 0-1.5zm0 6h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 1 1 0-1.5zm0 6h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 1 1 0-1.5z"></path></svg>
        </div>
        {showHamMenu && (
          <div className='ham-dropdown'>
            <div>home</div>
            <div>templates</div>
            <div>Tools</div>
            <div>Brand</div>
          </div>
        )}

        <div
          className='logo'
          onClick={() => window.location = '/designs'}
        >
          <img src={slate} width='80px' />
        </div>

        <button id='nav-title-buttons' onMouseOver={openDesMenu} >
          Design spotlight
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#484C4F" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
          {showDesMenu && (
            <div className='des-dropdown' onMouseLeave={closeDesMenu}>
              Past projects
              <a href='https://github.com/amanduhkv/Behrbnb' target="_blank" >
                Behrbnb
              </a>
              <a href='https://github.com/amanduhkv/Squeal' target="_blank" >
                Squeal
              </a>
            </div>
          )}
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
        <div id='user-initial' onClick={openProfMenu}>
          {sessionUser ? sessionUser.firstname[0] : <img src={avi} height='20px' />}
        </div>
        {showProfMenu && (
          <div className='profile-dropdown'>
            <div id='user-details'>
              <div id='icon-name'>
                <div id='user-initial-big'>
                  {sessionUser ? sessionUser.firstname[0] : <img src={avi} height='20px' />}
                </div>
                <h3 id='user-name'>
                  {sessionUser.firstname} {sessionUser.lastname}
                  <h5 id='user-email'>
                    {sessionUser.email}
                  </h5>
                </h3>
              </div>
            </div>
            <div id='logout'>
              <LogoutButton />
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}

export default NavBar;
