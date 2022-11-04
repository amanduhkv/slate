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
  useEffect(() => {
    const resultingTemp = document.getElementsByClassName('template')[0];
    console.log('RESULTING TEMPS', resultingTemp);
    if(singleDesign) {
      resultingTemp.style['background-color'] = backgroundColor
    }
  }, [backgroundColor])

  // LOADING TEMPLATES --------------------------------------------------
  let template;
  // let alias = template.alias;
  // let alias = singleDesign?.template?.[0].alias;
  // console.log('CURRENT ALIAS', alias)
  if (alias === 'presentation') {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white'
        }}
      >
        <div id='template-words'
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
        >
          <h1>Hello World!</h1>
          <p>You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!</p>
        </div>
      </div>
    )
  }
  if (alias === 'website') {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: `${backgroundColor}`
        }}
      >
        <div id='template-words'
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
        >
          <h1>Hello World!</h1>
          <p>You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!</p>
        </div>
      </div>
    )
  }
  if (alias === 'resume') {
    template = (
      <div
        className="template"
        style={{
          width: '637.5px',
          height: '825px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white'
        }}
      >
        <div id='template-words'
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
        >
          <h1>Hello World!</h1>
          <p>You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!</p>
        </div>
      </div>
    )
  }
  if (alias === 'igpost') {
    template = (
      <div
        className="template"
        style={{
          width: '480px',
          height: '480px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white'
        }}
      >
        <div id='template-words'
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
        >
          <h1>Hello World!</h1>
          <p>You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!</p>
        </div>
      </div>
    )
  }
  if (alias === 'igstory') {
    template = (
      <div
        className="template"
        style={{
          width: '270px',
          height: '480px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white'
        }}
      >
        <div id='template-words'
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
        >
          <h1>Hello World!</h1>
          <p>You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!</p>
        </div>
      </div>
    )
  }
  if (alias === 'fbpost') {
    template = (
      <div
        className="template"
        style={{
          width: '470px',
          height: '394px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white'
        }}
      >
        <div id='template-words'
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
        >
          <h1>Hello World!</h1>
          <p>You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!</p>
        </div>
      </div>
    )
  }
  if (alias === 'invitation') {
    template = (
      <div
        className="template"
        style={{
          width: '375px',
          height: '525px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white'
        }}
      >
        <div id='template-words'
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
        >
          <h1>Hello World!</h1>
          <p>You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!</p>
        </div>
      </div>
    )
  }
  if (alias === 'businesscard') {
    template = (
      <div
        className="template"
        style={{
          width: '336px',
          height: '192px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white'
        }}
      >
        <div id='template-words'
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
        >
          <h1>Hello World!</h1>
          <p>You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!</p>
        </div>
      </div>
    )
  }
  if (alias === 'infograph') {
    template = (
      <div
        className="template"
        style={{
          width: '200px',
          height: '500px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          backgroundColor: 'white'
        }}
      >
        <div id='template-words'>
          <h1
            style={{
              fontFamily: `${localStorage.getItem('font')}`
            }}
          >
            Hello World!
          </h1>
          <p
          style={{
            fontFamily: `${localStorage.getItem('font')}`
          }}
          >
            You can't add anything here yet, but try changing the template, font, or background color by clicking on the buttons in the sidebar!
          </p>
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
          <div id="inserted-temp">{template}</div>
        </div>
      </div>
      {/* {template} */}
    </div>
  )
}
