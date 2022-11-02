import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory, useLocation } from "react-router-dom";
import { getADesign, updateDesign, clearData } from "../../store/designs";

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

export default function SingleDesign() {
  const { designId } = useParams();
  const singleDesign = useSelector(state => state.designs.singleDesign);

  const history = useHistory();
  const dispatch = useDispatch();
  const url = useLocation().search;
  const alias = url.split('=')[1];
  // console.log('URL', url)

  const [name, setName] = useState('');
  const [validationErrs, setValidationErrs] = useState([]);
  const [hasSubmit, setHasSubmit] = useState(false);
  const [showSideMenu, setShowSideMenu] = useState(false);
  const [showEleMenu, setShowEleMenu] = useState(false);



  useEffect(() => {
    dispatch(getADesign(designId))

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

  const openEleMenu = () => {
    if (showEleMenu) return;
    setShowEleMenu(true);
  };

  useEffect(() => {
    if (!showEleMenu) return;
    const closeEleMenu = () => {
      setShowEleMenu(false);
    };
    document.addEventListener('click', closeEleMenu);
    return () => document.removeEventListener("click", closeEleMenu);
  }, [showEleMenu]);


  // LOADING TEMPLATES --------------------------------------------------
  let template;
  // let alias = singleDesign?.template?.[0].alias;
  // console.log('CURRENT ALIAS', alias)
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
      name: name,
      template: alias
    };

    if (!validationErrs.length) {
      let updatedDes = await dispatch(updateDesign(payload));

      if (updatedDes) history.push(`/designs/${updatedDes.id}/?temp=${alias}`);
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
        <input
          id='des-name'
          type='text'
          placeholder={singleDesign.name}
          value={name}
          onChange={e => setName(e.target.value)}
        />

        <button id='create-des-button' type='submit'>Save design</button>
        <DeleteDesign />
        </div>
      </form>
      <div className="edit-container">
        <div className="sidebar">
          <button onClick={openSideMenu}>Templates</button>
          {showSideMenu && (
            <div className="temp-menu-container">
              {/* <div id='warning'>Warning: Switching templates deletes any previous work made.</div> */}
              <div id='temp-menu-item'>
                {singleDesign.template.map(temp => (
                  <div id='temp-container-des' onClick={() => history.push(`/designs/${designId}?temp=${temp.alias}`)}>
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

          <button onClick={openEleMenu}>Elements</button>
          {showEleMenu && (
            <div id='temp-menu-item'>
              elements here
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
      {/* {template} */}
    </div>
  )
}
