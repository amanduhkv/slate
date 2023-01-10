import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllDesigns, clearData } from "../../store/designs";

import pres from '../../icons/pres.png';
import web from '../../icons/website.png';
import ig from '../../icons/ig.png';
import invite from '../../icons/invite.png';

import imgs from './templateImages';

import './index.css';
import NavBar from "../NavBar";
import { useHistory } from "react-router-dom";
import UserDesigns from "./UserDesigns";

export default function Designs() {
  const designs = useSelector(state => state.designs.allDesigns);
  const designArr = Object.values(designs);


  const history = useHistory();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllDesigns())

    return () => dispatch(clearData())
  }, [dispatch])

  let tempNames = {
    'presentation': 'pres',
    'website': 'web',
    'resume': 'res',
    'igpost': 'ig',
    'igstory': 'igs',
    'fbpost': 'fb',
    'invitation': 'inv',
    'businesscard': 'biz',
    'infograph': 'info'
    };
  let tempDescriptions = ['original', 'fun', 'aesthetic', 'green', 'bw'];

  let allTemplates = {}

  Object.keys(tempNames).forEach(tempName => {
    tempDescriptions.forEach((tempDesc, idx)=> {
      allTemplates[`${tempName}-${tempDesc}`] = `${tempNames[tempName]}${idx + 1}`
    })
  });
  delete allTemplates['igstory-bw']
  allTemplates['igstory-pink'] = 'igs5'


  return (
    <div>
      <NavBar />
      <div className="title-box">
        <h1 id='box-title'>Thanks for being you!</h1>
        <div className="box-temp-buttons-container">
          <div id='temp-button-container'>
            <button
              id='box-temp-buttons'
              onClick={() => history.push('/designs/new/presentation')}
            >
              <img src={pres} alt='presentation-icon' width='30px' height='30px' />
            </button>
            <div id='temp-text'>Presentation</div>
          </div>
          <div id='temp-button-container'>
            <button
              id='box-temp-buttons'
              onClick={() => history.push('/designs/new/website')}
            >
              <img src={web} alt='website-icon' width='30px' height='30px' />
            </button>
            <div id='temp-text'>Website</div>
          </div>
          <div id='temp-button-container'>
            <button
              id='box-temp-buttons'
              onClick={() => history.push('/designs/new/igpost')}
            >
              <img src={ig} alt='ig-icon' width='30px' height='30px' />
            </button>
            <div id='temp-text'>Instagram Post</div>
          </div>
          <div id='temp-button-container'>
            <button
              id='box-temp-buttons'
              onClick={() => history.push('/designs/new/invitation')}
            >
              <img src={invite} alt='invitation-icon' width='30px' height='30px' />
            </button>
            <div id='temp-text'>Invitation</div>
          </div>
        </div>
      </div>


      <div className="temp-box-container">
        <h3>You might want to try...</h3>
        <div className="temp-cards">
          {/* <button
            id='left-arrow'
            type='button'
            onClick={() => document.getElementById('temp-box').scrollLeft += 20}
          >
            left
          </button> */}
          <div id='temp-box'>
            {designArr[0]?.template.map(temp => (
              <div className="temp-box" onClick={() => history.push(`/designs/new/${temp.alias}`)}>
                <div>
                  {
                    <img id='temp-img' src={imgs[allTemplates[temp.alias]]} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} />

                  }
                  <div>{temp.alias ? temp.name : null}</div>
                </div>
              </div>
            ))}
          </div>
          {/* <button
            id='right-arrow'
            type='button'
            onClick={() => document.getElementById('temp-box').scrollRight += 5}
          >
            right
          </button> */}
        </div>
      </div>


      <div className="recent-container">
        <h2>Recent designs</h2>
        <div>
          <UserDesigns />
        </div>
      </div>
    </div>
  )
}
