import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllDesigns, clearData } from "../../store/designs";

import pres from '../../icons/pres.png';
import web from '../../icons/website.png';
import ig from '../../icons/ig.png';
import invite from '../../icons/invite.png';
import present from '../../icons/temps/presentation.png';
import website from '../../icons/temps/website.png';
import resume from '../../icons/temps/resume.png';
import igpost from '../../icons/temps/igpost.png';
import igstory from '../../icons/temps/igstory.png';
import fbpost from '../../icons/temps/fbpost.png';
import inv from '../../icons/temps/invitation.png';
import bizcard from '../../icons/temps/businesscard.png';
import info from '../../icons/temps/infograph.png';

import pres1 from '../../icons/change-temps/present-temp/pres-original.svg';
import pres2 from '../../icons/change-temps/present-temp/pres-fun.svg';
import pres3 from '../../icons/change-temps/present-temp/pres-aesthetic.svg';
import pres4 from '../../icons/change-temps/present-temp/pres-green.svg';
import pres5 from '../../icons/change-temps/present-temp/pres-bw.svg';

import web1 from '../../icons/change-temps/website-temp/website-original.png';
import web2 from '../../icons/change-temps/website-temp/website-fun.png';
import web3 from '../../icons/change-temps/website-temp/website-aesthetic.png';
import web4 from '../../icons/change-temps/website-temp/website-green.png';
import web5 from '../../icons/change-temps/website-temp/website-bw.png';

import ig1 from '../../icons/change-temps/ig-temp/ig-original.svg';
import ig2 from '../../icons/change-temps/ig-temp/ig-fun.svg';
import ig3 from '../../icons/change-temps/ig-temp/ig-aesthetic.svg';
import ig4 from '../../icons/change-temps/ig-temp/ig-green.svg';
import ig5 from '../../icons/change-temps/ig-temp/ig-bw.svg';

import igs1 from '../../icons/change-temps/igs-temp/igs-original.svg';
import igs2 from '../../icons/change-temps/igs-temp/igs-fun.svg';
import igs3 from '../../icons/change-temps/igs-temp/igs-aesthetic.svg';
import igs4 from '../../icons/change-temps/igs-temp/igs-green.svg';
import igs5 from '../../icons/change-temps/igs-temp/igs-pink.svg';

import fb1 from '../../icons/change-temps/fb-temp/fb-original.svg';
import fb2 from '../../icons/change-temps/fb-temp/fb-fun.svg';
import fb3 from '../../icons/change-temps/fb-temp/fb-aesthetic.svg';
import fb4 from '../../icons/change-temps/fb-temp/fb-green.svg';
import fb5 from '../../icons/change-temps/fb-temp/fb-bw.svg';

import inv1 from '../../icons/change-temps/invite-temp/invite-original.svg';
import inv2 from '../../icons/change-temps/invite-temp/invite-fun.svg';
import inv3 from '../../icons/change-temps/invite-temp/invite-aesthetic.svg';
import inv4 from '../../icons/change-temps/invite-temp/invite-green.svg';
import inv5 from '../../icons/change-temps/invite-temp/invite-bw.svg';

import biz1 from '../../icons/change-temps/bizcard-temp/bizcard-original.svg';
import biz2 from '../../icons/change-temps/bizcard-temp/bizcard-fun.svg';
import biz3 from '../../icons/change-temps/bizcard-temp/bizcard-aesthetic.svg';
import biz4 from '../../icons/change-temps/bizcard-temp/bizcard-green.svg';
import biz5 from '../../icons/change-temps/bizcard-temp/bizcard-bw.svg';

import info1 from '../../icons/change-temps/info-temp/info-original.svg';
import info2 from '../../icons/change-temps/info-temp/info-fun.svg';
import info3 from '../../icons/change-temps/info-temp/info-aesthetic.svg';
import info4 from '../../icons/change-temps/info-temp/info-green.svg';
import info5 from '../../icons/change-temps/info-temp/info-bw.svg';

import res1 from '../../icons/change-temps/res-temp/res-original.svg';
import res2 from '../../icons/change-temps/res-temp/res-fun.svg';
import res3 from '../../icons/change-temps/res-temp/res-aesthetic.svg';
import res4 from '../../icons/change-temps/res-temp/res-green.svg';
import res5 from '../../icons/change-temps/res-temp/res-bw.svg';

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
                  {temp.alias === 'presentation-original' ?
                    <img id='temp-img' src={pres1} alt='pres' width='160px' /> :
                    temp.alias === 'presentation-fun' ?
                      <img id='temp-img' src={pres2} alt='pres' width='160px' /> :
                    temp.alias === 'presentation-aesthetic' ?
                      <img id='temp-img' src={pres3} alt='pres' width='160px' /> :
                    temp.alias === 'presentation-green' ?
                      <img id='temp-img' src={pres4} alt='pres' width='160px' /> :
                    temp.alias === 'presentation-bw' ?
                      <img id='temp-img' src={pres5} alt='pres' width='160px' /> :
                    temp.alias === 'website-original' ?
                      <img id='temp-img' src={web1} alt='pres' width='160px' /> :
                    temp.alias === 'website-fun' ?
                      <img id='temp-img' src={web2} alt='pres' width='160px' /> :
                    temp.alias === 'website-aesthetic' ?
                      <img id='temp-img' src={web3} alt='pres' width='160px' /> :
                    temp.alias === 'website-green' ?
                      <img id='temp-img' src={web4} alt='pres' width='160px' /> :
                    temp.alias === 'website-bw' ?
                      <img id='temp-img' src={web5} alt='pres' width='160px' /> :
                      // temp.alias === 'resume' ?
                      //   <img id='temp-img' src={resume} alt='pres' width='160px' /> :
                      // temp.alias === 'resume' ?
                      //   <img id='temp-img' src={resume} alt='pres' width='160px' /> :
                      // temp.alias === 'resume' ?
                      //   <img id='temp-img' src={resume} alt='pres' width='160px' /> :
                      // temp.alias === 'resume' ?
                      //   <img id='temp-img' src={resume} alt='pres' width='160px' /> :
                      // temp.alias === 'resume' ?
                      //   <img id='temp-img' src={resume} alt='pres' width='160px' /> :
                      //   temp.alias === 'igpost' ?
                      //     <img id='temp-img' src={igpost} alt='pres' width='160px' /> :
                      //     temp.alias === 'igstory' ?
                      //       <img id='temp-img' src={igstory} alt='pres' width='160px' /> :
                      //       temp.alias === 'fbpost' ?
                      //         <img id='temp-img' src={fbpost} alt='pres' width='160px' /> :
                      //         temp.alias === 'invitation' ?
                      //           <img id='temp-img' src={inv} alt='pres' width='160px' /> :
                      //           temp.alias === 'businesscard' ?
                      //             <img id='temp-img' src={bizcard} alt='pres' width='160px' /> :
                      //             temp.alias === 'infograph' ?
                      //               <img id='temp-img' src={info} alt='pres' width='160px' /> :
                                    "Your template here"
                  }
                  <div>{temp.name}</div>
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
