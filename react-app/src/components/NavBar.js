import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import { getAllDesigns, clearData } from "../store/designs";

import './NavBar.css';

import slate from '../icons/slate.png';
import avi from '../icons/avi.svg';


const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user);
  const designs = useSelector(state => state.designs.allDesigns);

  const [showProfMenu, setShowProfMenu] = useState(false);
  const [showHamMenu, setShowHamMenu] = useState(false);
  const [showDesMenu, setShowDesMenu] = useState(false);
  const [showCreateMenu, setShowCreateMenu] = useState(false);
  const history = useHistory();

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllDesigns())

    return () => dispatch(clearData())
  }, [dispatch])

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
  const openCreateMenu = () => {
    if (showCreateMenu) return;
    setShowCreateMenu(true);
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

  useEffect(() => {
    if (!showCreateMenu) return;
    const closeCreateMenu = () => {
      setShowCreateMenu(false);
    };
    document.addEventListener('click', closeCreateMenu);
    return () => document.removeEventListener("click", closeCreateMenu);
  }, [showCreateMenu]);


  return (
    <nav>
      <div className='left-nav'>

        <div id='hamburger' onClick={openHamMenu}>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5.75 5.25h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 0 1 0-1.5zm0 6h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 1 1 0-1.5zm0 6h12.5a.75.75 0 1 1 0 1.5H5.75a.75.75 0 1 1 0-1.5z"></path></svg>
        </div>
        {showHamMenu && (
          <div className='ham-dropdown'>
            <div
              id='ham-dd-content'
              onClick={() => history.push('/')}
            >
              Home
            </div>
            {/* <div>Templates</div>
            <div>Tools</div> */}
            <div
              id='ham-dd-content'
              onClick={() => history.push('/brand')}
            >
              Brand
            </div>
          </div>
        )}

        <div
          className='logo'
          onClick={() => window.location = '/designs'}
        >
          <img src={slate} width='80px' alt='logo' />
        </div>

        <button id='nav-title-buttons' onMouseOver={openDesMenu} >
          Dev spotlight
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="#484C4F" d="m11.71 6.47-3.53 3.54c-.1.1-.26.1-.36 0L4.3 6.47a.75.75 0 1 0-1.06 1.06l3.53 3.54c.69.68 1.8.68 2.48 0l3.53-3.54a.75.75 0 0 0-1.06-1.06z"></path></svg>
          {showDesMenu && (
            <div onMouseLeave={closeDesMenu}>
              <div className='des-dropdown' >
                <div>Past projects</div>
                <a href='https://github.com/amanduhkv/Behrbnb' target="_blank" rel="noreferrer">
                  Behrbnb
                </a>
                <a href='https://github.com/amanduhkv/Squeal' target="_blank" rel="noreferrer">
                  Squeal
                </a>

                <div>Links</div>
                <a href='https://github.com/amanduhkv/' target="_blank" rel="noreferrer">
                  Github
                </a>
                <a href='https://www.linkedin.com/in/amandakvien/' target="_blank" rel="noreferrer">
                  LinkedIn
                </a>
              </div>

            </div>
          )}
        </button>
        {/* <button id='nav-title-buttons'>
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
        </button> */}
      </div>

      <div className='right-nav'>
        <button
          onClick={openCreateMenu}
        >
          Create a design
        </button>
        {showCreateMenu && (
          <div className='create-dropdown'>
            {Object.values(designs)[0]?.template.map(temp => (
              <div
                onClick={() => history.push(`/designs/new/${temp.alias}`)}
                id='temp-name'
              >
                {temp.name}
              </div>
            ))}
          </div>
        )}
        <div id='user-initial' onClick={openProfMenu}>
          {sessionUser ? sessionUser.firstname[0] : <img src={avi} height='20px' alt='avatar' />}
        </div>
        {showProfMenu && (
          <div className='profile-dropdown'>
            <div id='user-details'>
              <div id='icon-name'>
                <div id='user-initial-big'>
                  {sessionUser ? sessionUser.firstname[0] : <img src={avi} height='20px' alt='avatar' />}
                </div>
                <div id='user-name'>
                  {sessionUser.firstname} {sessionUser.lastname}
                  <h5 id='user-email'>
                    {sessionUser.email}
                  </h5>
                </div>
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
