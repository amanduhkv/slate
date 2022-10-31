import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllDesigns, clearData } from "../../store/designs";

import pres from '../../icons/pres.png';
import web from '../../icons/website.png';
import ig from '../../icons/ig.png';
import invite from '../../icons/invite.png';
import squiggles from '../../icons/squiggles.png';
import './index.css';
import NavBar from "../NavBar";

export default function Designs() {
  const designs = useSelector(state => state.designs.allDesigns);
  const designArr = Object.values(designs);

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllDesigns())

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div>
      <NavBar />
      <div className="title-box">
        <h1 id='box-title'>Thanks for being you!</h1>
        <div className="box-temp-buttons-container">
          <div id='temp-button-container'>
            <button
              id='box-temp-buttons'
              onClick={() => window.location = '/designs/new/presentation'}
            >
              <img src={pres} alt='presentation-icon' width='30px' height='30px' />
            </button>
            <div id='temp-text'>Presentation</div>
          </div>
          <div id='temp-button-container'>
            <button
              id='box-temp-buttons'
              onClick={() => window.location = '/designs/new/website'}
            >
              <img src={web} alt='website-icon' width='30px' height='30px' />
            </button>
            <div id='temp-text'>Website</div>
          </div>
          <div id='temp-button-container'>
            <button
              id='box-temp-buttons'
              onClick={() => window.location = '/designs/new/igpost'}
            >
              <img src={ig} alt='ig-icon' width='30px' height='30px' />
            </button>
            <div id='temp-text'>Instagram Post</div>
          </div>
          <div id='temp-button-container'>
            <button
              id='box-temp-buttons'
              onClick={() => window.location = '/designs/new/invitation'}
            >
              <img src={invite} alt='invitation-icon' width='30px' height='30px' />
            </button>
            <div id='temp-text'>Invitation</div>
          </div>
        </div>
      </div>
      <div>
        <h3>You might want to try...</h3>
      </div>
      <div>
        <h2>Recent designs</h2>
      </div>
    </div>
  )
}
