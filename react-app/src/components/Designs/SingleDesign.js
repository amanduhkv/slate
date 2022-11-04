import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory, useLocation } from "react-router-dom";
import { getADesign, updateDesign, clearData, getAllDesigns } from "../../store/designs";
import { getAllBrands } from "../../store/brands"

import left from '../../icons/left.svg';
import present from '../../icons/temps/presentation.png';
import website from '../../icons/temps/website.png';
import resume from '../../icons/temps/resume.png';
import igpost from '../../icons/temps/igpost.png';
import igstory from '../../icons/temps/igstory.png';
import fbpost from '../../icons/temps/fbpost.png';
import inv from '../../icons/temps/invitation.png';
import bizcard from '../../icons/temps/businesscard.png';
import info from '../../icons/temps/infograph.png';
import DeleteDesign from "../DeleteDesignForm";

import pres1 from '../../icons/change-temps/present-temp/pres-original.svg';
import pres2 from '../../icons/change-temps/present-temp/pres-fun.svg';
import pres3 from '../../icons/change-temps/present-temp/pres-aesthetic.svg';
import pres4 from '../../icons/change-temps/present-temp/pres-green.svg';
import pres5 from '../../icons/change-temps/present-temp/pres-bw.svg';

import web1 from '../../icons/change-temps/website-temp/web-original.png';
import web2 from '../../icons/change-temps/website-temp/web-fun.png';
import web3 from '../../icons/change-temps/website-temp/web-aesthetic.png';
import web4 from '../../icons/change-temps/website-temp/web-green.png';
import web5 from '../../icons/change-temps/website-temp/web-bw.png';

import ig1 from '../../icons/change-temps/ig-temp/ig-original.svg';
import ig2 from '../../icons/change-temps/ig-temp/ig-fun.svg';
import ig3 from '../../icons/change-temps/ig-temp/ig-aesthetic.svg';
import ig4 from '../../icons/change-temps/ig-temp/ig-green.svg';
import ig5 from '../../icons/change-temps/ig-temp/ig-bw.svg';

import igs1 from '../../icons/change-temps/ig-story-temp/igs-original.svg';
import igs2 from '../../icons/change-temps/ig-story-temp/igs-fun.svg';
import igs3 from '../../icons/change-temps/ig-story-temp/igs-aesthetic.svg';
import igs4 from '../../icons/change-temps/ig-story-temp/igs-green.svg';
import igs5 from '../../icons/change-temps/ig-story-temp/igs-pink.svg';

import fb1 from '../../icons/change-temps/fb-temp/fb-original.svg';
import fb2 from '../../icons/change-temps/fb-temp/fb-fun.svg';
import fb3 from '../../icons/change-temps/fb-temp/fb-aesthetic.svg';
import fb4 from '../../icons/change-temps/fb-temp/fb-green.svg';
import fb5 from '../../icons/change-temps/fb-temp/fb-bw.svg';

import inv1 from '../../icons/change-temps/invite-temp/inv-original.svg';
import inv2 from '../../icons/change-temps/invite-temp/inv-fun.svg';
import inv3 from '../../icons/change-temps/invite-temp/inv-aesthetic.svg';
import inv4 from '../../icons/change-temps/invite-temp/inv-green.svg';
import inv5 from '../../icons/change-temps/invite-temp/inv-bw.svg';

import biz1 from '../../icons/change-temps/bizcard-temp/biz-original.svg';
import biz2 from '../../icons/change-temps/bizcard-temp/biz-fun.svg';
import biz3 from '../../icons/change-temps/bizcard-temp/biz-aesthetic.svg';
import biz4 from '../../icons/change-temps/bizcard-temp/biz-green.svg';
import biz5 from '../../icons/change-temps/bizcard-temp/biz-bw.svg';

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

export default function SingleDesign() {
  const { designId } = useParams();
  const singleDesign = useSelector(state => state.designs.singleDesign);
  const allDesigns = useSelector(state => state.designs.allDesigns);
  const brands = useSelector(state => state.brands.allBrands);
  const user = useSelector(state => state.session.user);

  const history = useHistory();
  const dispatch = useDispatch();
  const url = useLocation().pathname.split('/');
  let alias = url[3];
  // console.log('URL', url)

  const [name, setName] = useState('');
  const [temp, setTemp] = useState('');
  const [validationErrs, setValidationErrs] = useState([]);
  const [hasSubmit, setHasSubmit] = useState(false);
  const [showSideMenu, setShowSideMenu] = useState(false);
  const [showBrandMenu, setShowBrandMenu] = useState(false);
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [input3, setInput3] = useState('');
  const [input4, setInput4] = useState('');
  const [input5, setInput5] = useState('');

  const [backgroundColor, setBackgroundColor] = useState('white');
  const [currFont, setCurrFont] = useState('');

  useEffect(() => {
    dispatch(getADesign(designId))
    dispatch(getAllDesigns());
    dispatch(getAllBrands());

    return () => dispatch(clearData())
  }, [dispatch, designId])


  // SIDEBAR MENU FXNS ---------------------------------------------
  const openSideMenu = () => {
    if (showSideMenu) return;
    setShowSideMenu(true);
  };

  useEffect(() => {
    if (!showSideMenu) return;
    const closeSideMenu = () => {
      setShowSideMenu(false);
    };
    document.addEventListener('click', closeSideMenu);
    return () => document.removeEventListener("click", closeSideMenu);
  }, [showSideMenu]);

  const openBrandMenu = () => {
    if (showBrandMenu) return;
    setShowBrandMenu(true);
  };

  useEffect(() => {
    if (!showBrandMenu) return;
    const closeBrandMenu = () => {
      setShowBrandMenu(false);
    };
    document.addEventListener('click', closeBrandMenu);
    return () => document.removeEventListener("click", closeBrandMenu);
  }, [showBrandMenu]);

  // CHANGING BCKGD COLOR FXNS ------------------------------------------
  // useEffect(() => {
  //   const resultingTemp = document.getElementsByClassName('template')[0];
  //   console.log('RESULTING TEMPS', resultingTemp);
  //   if(singleDesign) {
  //     resultingTemp.style['background-color'] = backgroundColor
  //   }
  // }, [backgroundColor])

  // LOADING TEMPLATES --------------------------------------------------
  let template;

  if (alias.includes('presentation')) {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white',
          backgroundImage: `url(${alias.includes('original') ? pres1 :
            alias.includes('fun') ? pres2 :
              alias.includes('aesthetic') ? pres3 :
                alias.includes('green') ? pres4 :
                  alias.includes('bw') ? pres5 :
                    null
            })`
        }}
      >
      </div>
    )
  }
  if (alias.includes('website')) {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: `${backgroundColor}`,
          backgroundImage: `url(${alias.includes('original') ? web1 :
            alias.includes('fun') ? web2 :
              alias.includes('aesthetic') ? web3 :
                alias.includes('green') ? web4 :
                  alias.includes('bw') ? web5 :
                    null
            })`
        }}
      >

      </div>
    )
  }
  if (alias.includes('resume')) {
    template = (
      <div
        className="template"
        style={{
          width: '637.5px',
          height: '825px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white',
          backgroundImage: `url(${alias.includes('original') ? res1 :
            alias.includes('fun') ? res2 :
              alias.includes('aesthetic') ? res3 :
                alias.includes('green') ? res4 :
                  alias.includes('bw') ? res5 :
                    null
            })`
        }}
      >

      </div>
    )
  }
  if (alias.includes('igpost')) {
    template = (
      <div
        className="template"
        style={{
          width: '480px',
          height: '480px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white',
          backgroundImage: `url(${alias.includes('original') ? ig1 :
            alias.includes('fun') ? ig2 :
              alias.includes('aesthetic') ? ig3 :
                alias.includes('green') ? ig4 :
                  alias.includes('bw') ? ig5 :
                    null
            })`
        }}
      >

      </div>
    )
  }
  if (alias.includes('igstory')) {
    template = (
      <div
        className="template"
        style={{
          width: '270px',
          height: '480px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white',
          backgroundImage: `url(${alias.includes('original') ? igs1 :
            alias.includes('fun') ? igs2 :
              alias.includes('aesthetic') ? igs3 :
                alias.includes('green') ? igs4 :
                  alias.includes('pink') ? igs5 :
                    null
            })`
        }}
      >

      </div>
    )
  }
  if (alias.includes('fbpost')) {
    template = (
      <div
        className="template"
        style={{
          width: '470px',
          height: '394px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white',
          backgroundImage: `url(${alias.includes('original') ? fb1 :
            alias.includes('fun') ? fb2 :
              alias.includes('aesthetic') ? fb3 :
                alias.includes('green') ? fb4 :
                  alias.includes('bw') ? fb5 :
                    null
            })`
        }}
      >

      </div>
    )
  }
  if (alias.includes('invitation')) {
    template = (
      <div
        className="template"
        style={{
          width: '375px',
          height: '525px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white',
          backgroundImage: `url(${alias.includes('original') ? inv1 :
            alias.includes('fun') ? inv2 :
              alias.includes('aesthetic') ? inv3 :
                alias.includes('green') ? inv4 :
                  alias.includes('bw') ? inv5 :
                    null
            })`
        }}
      >

      </div>
    )
  }
  if (alias.includes('businesscard')) {
    template = (
      <div
        className="template"
        style={{
          width: '336px',
          height: '192px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white',
          backgroundImage: `url(${alias.includes('original') ? biz1 :
            alias.includes('fun') ? biz2 :
              alias.includes('aesthetic') ? biz3 :
                alias.includes('green') ? biz4 :
                  alias.includes('bw') ? biz5 :
                    null
            })`
        }}
      >

      </div>
    )
  }
  if (alias.includes('infograph')) {
    template = (
      <div
        className="template"
        style={{
          width: '200px',
          height: '500px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white',
          backgroundImage: `url(${alias.includes('original') ? info1 :
            alias.includes('fun') ? info2 :
              alias.includes('aesthetic') ? info3 :
                alias.includes('green') ? info4 :
                  alias.includes('bw') ? info5 :
                    null
            })`
        }}
      >
        <div>
          <input
            type='text'
            value={input1}
            onChange={(e) => setInput1(e.target.value)}
          />
        </div>
      </div>
    )
  }

  // // LOADING PREV DATA ---------------------------------------
  // useEffect(() => {
  //   if(singleDesign) {
  //     setName(singleDesign.name);
  //     setTemp(singleDesign.template[0])
  //   }
  // }, [singleDesign])

  // SUBMIT FXNS ---------------------------------------------
  useEffect(() => {
    const errors = [];

    if (!name.length) errors.push('Please confirm these changes by re-entering the name for this design, or entering a new name for the design.')
    setValidationErrs(errors);
  }, [name]);

  const handleSubmit = async e => {
    e.preventDefault();

    setHasSubmit(true);

    const payload = {
      name: name,
      template: alias
    };

    if (!validationErrs.length) {
      let updatedDes = await dispatch(updateDesign(singleDesign.id, payload));
      console.log('updatedDes', updatedDes)

      if (updatedDes) history.push(`/designs`);
    };
  };


  if (!singleDesign) return null;

  return (
    <div>
      <form className='create-des-form' onSubmit={handleSubmit}>
        <div id='home-button' onClick={() => history.push('/designs')}>
          <img src={left} alt='left' height='14px' />
          Home
        </div>

        <div>
          {hasSubmit && validationErrs.length > 0 && (
            <div className='errors' id='des-errs'>
              {validationErrs.map((error, idx) => (
                <div key={idx}>{error}</div>
              ))}
            </div>
          )}
          <input
            id='des-name'
            type='text'
            placeholder={singleDesign.name}
            value={name}
            onChange={e => setName(e.target.value)}
          />
          <input
            type='text'
            value={temp}
            hidden
            onChange={e => setTemp(e.target.value)}
          />
          {user && user.id === singleDesign.user_id && (
            <>
              <button id='create-des-button' type='submit'>Save design</button>
              <DeleteDesign />
            </>
          )}
        </div>
      </form>
      <div className="edit-container">
        <div className="sidebar">
          <button onClick={openSideMenu}>Templates</button>
          {showSideMenu && (
            <div className="temp-menu-container">
              {/* <div id='warning'>Warning: Switching templates deletes any previous work made.</div> */}
              <div id='temp-menu-item'>
                {allDesigns[1].template.map(temp => (
                  <div id='temp-container-des' onClick={() => {
                    setTemp(temp)
                    history.push(`/designs/${designId}/${temp.alias}`)
                  }}>
                    {temp.alias === 'presentation' ?
                      <img id='temp-img-des' src={present} alt='pres' width='130px' /> :
                      temp.alias === 'website' ?
                        <img id='temp-img-des' src={website} alt='pres' width='130px' /> :
                        temp.alias === 'resume' ?
                          <img id='temp-img-des' src={resume} alt='pres' width='130px' /> :
                          temp.alias === 'igpost' ?
                            <img id='temp-img-des' src={igpost} alt='pres' width='130px' /> :
                            temp.alias === 'igstory' ?
                              <img id='temp-img-des' src={igstory} alt='pres' width='130px' /> :
                              temp.alias === 'fbpost' ?
                                <img id='temp-img-des' src={fbpost} alt='pres' width='130px' /> :
                                temp.alias === 'invitation' ?
                                  <img id='temp-img-des' src={inv} alt='pres' width='130px' /> :
                                  temp.alias === 'businesscard' ?
                                    <img id='temp-img-des' src={bizcard} alt='pres' width='130px' /> :
                                    temp.alias === 'infograph' ?
                                      <img id='temp-img-des' src={info} alt='pres' width='130px' /> :
                                      "Your template here"
                    }
                    <button id='create-des-temp-button'>{temp.name}</button>
                  </div>
                ))}

              </div>

            </div>
          )}

          <button onClick={openBrandMenu}>Brands</button>
          {showBrandMenu && (
            <div id='temp-menu-item-brand'>
              Oops! Looks like this feature is still in the works.
            </div>
            // <div id='temp-menu-item'>
            //   {Object.values(brands).map(brand => (
            //     <div className="des-brand-colors">
            //       {brand.colors.map(color => (
            //         <div
            //           onClick={() => {
            //             setBackgroundColor(color.name);
            //             localStorage.setItem('backgroundColor', color.name)
            //           }}
            //         >{color.name}</div>
            //       ))}
            //       {brand.fonts.map(font => (
            //         <div
            //           onClick={() => {
            //             setCurrFont(font.name);
            //           }}
            //         >
            //           {font.name}
            //         </div>
            //       ))}
            //     </div>
            //   ))}
            // </div>
          )}
        </div>

        <div className="edit-area">
          <div id="inserted-temp">
            {template}
          </div>
        </div>
      </div>
      {/* {template} */}
    </div>
  )
}
