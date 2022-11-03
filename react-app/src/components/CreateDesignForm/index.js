import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import { createDesign, getAllDesigns, clearData } from "../../store/designs";

import './CreateDesignForm.css';

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
import { getAllBrands } from "../../store/brands";

export default function CreateDesign() {
  const dispatch = useDispatch();
  const history = useHistory();
  const url = useLocation().pathname;
  // console.log('CURRENT URL: ', url)
  const designs = useSelector(state => state.designs.allDesigns);
  const templates = Object.values(designs)[0]?.template;
  // console.log(templates)
  const brands = useSelector(state => state.brands.allBrands);

  let alias = url.split('/')[3]
  // console.log('Alias', alias)
  const [name, setName] = useState('');
  const [temp, setTemp] = useState('');
  const [validationErrs, setValidationErrs] = useState([]);
  const [hasSubmit, setHasSubmit] = useState(false);
  const [showSideMenu, setShowSideMenu] = useState(false);
  const [showBrandMenu, setShowBrandMenu] = useState(false);

  useEffect(() => {
    dispatch(getAllDesigns());
    dispatch(getAllBrands());
    return () => dispatch(clearData())
  }, [dispatch])

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

  // SUBMIT FXNS ---------------------------------------------
  useEffect(() => {
    const errors = [];

    if (!name.length) errors.push('Please enter a name for the design.')
    setValidationErrs(errors);
  }, [name]);

  const handleSubmit = async e => {
    e.preventDefault();

    setHasSubmit(true);

    const payload = {
      name,
      template: alias
    };

    if (!validationErrs.length) {
      let createdDes = await dispatch(createDesign(payload));
      console.log('template', alias)
      if (createdDes) history.push(`/designs/${createdDes.id}/${alias}`);
    };
  };

  // LOADING TEMPLATES --------------------------------------------------
  let template;
  if (alias === 'presentation') {
    template = (
      <div
        style={{
          width: '960px',
          height: '540px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }
  if (alias === 'website') {
    template = (
      <div
        style={{
          width: '683px',
          height: '384px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }
  if (alias === 'resume') {
    template = (
      <div
        style={{
          width: '637.5px',
          height: '825px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }
  if (alias === 'igpost') {
    template = (
      <div
        style={{
          width: '480px',
          height: '480px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }
  if (alias === 'igstory') {
    template = (
      <div
        style={{
          width: '270px',
          height: '480px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }
  if (alias === 'fbpost') {
    template = (
      <div
        style={{
          width: '470px',
          height: '394px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }
  if (alias === 'invitation') {
    template = (
      <div
        style={{
          width: '375px',
          height: '525px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }
  if (alias === 'businesscard') {
    template = (
      <div
        style={{
          width: '336px',
          height: '192px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }
  if (alias === 'infograph') {
    template = (
      <div
        style={{
          width: '200px',
          height: '500px',
          backgroundColor: 'white',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        }}
      >
      </div>
    )
  }

  return (
    <div>
      <form className='create-des-form' onSubmit={handleSubmit}>
        <div id='home-button' onClick={() => history.push('/designs')}>
          <img src={left} alt='left' height='14px' />
          Home
        </div>
        <div>
        <input
          id='des-name'
          type='text'
          placeholder="Design title"
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <input
          type='text'
          value={temp}
          hidden
          onChange={e => setTemp(e.target.value)}
        />
        <button id='create-des-button' type='submit'>Save new design</button>
        </div>
      </form>

      <div className="edit-container">
        <div className="sidebar">
          <button onClick={openSideMenu}>Templates</button>
          {showSideMenu && (
            <div className="temp-menu-container">
              {/* <div id='warning'>Warning: Switching templates deletes any previous work made.</div> */}
              <div id='temp-menu-item'>
                {templates.map(temp => (
                  <div id='temp-container-des' onClick={() => {
                    // console.log('TEMP', temp)
                    setTemp(temp)
                    history.push(`/designs/new/${temp.alias}`)
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
            <div id='temp-menu-item'>
              {Object.values(brands).map(brand => (
                <div className="des-brand-colors">
                  {brand.colors.map(color => (
                  <div>{color.name}</div>
                  ))}
                  {brand.fonts.map(font => (
                    <div>
                      {font.name}
                    </div>
                  ))}
                </div>
              ))}
            </div>
          )}
          {/* <button onClick={openSideMenu}>Text</button>
        <button onClick={openSideMenu}>Styles</button>
        <button onClick={openSideMenu}>Logos</button> */}
        </div>

        <div className="edit-area">
          <div id="inserted-temp">{template}</div>

        </div>
      </div>
    </div>
  )

}
