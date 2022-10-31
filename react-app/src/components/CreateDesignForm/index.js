import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import { createDesign, getAllDesigns, clearData } from "../../store/designs";

import './CreateDesignForm.css';

export default function CreateDesign() {
  const dispatch = useDispatch();
  const history = useHistory();
  const url = useLocation().pathname;
  // console.log('CURRENT URL: ', url)
  const designs = useSelector(state => state.designs.allDesigns);
  const templates = Object.values(designs)[0]?.template;
  // console.log(templates)

  let alias = url.split('/')[3]
  // console.log('Alias', alias)
  const [name, setName] = useState('');
  const [validationErrs, setValidationErrs] = useState([]);
  const [hasSubmit, setHasSubmit] = useState(false);
  const [showSideMenu, setShowSideMenu] = useState(false);
  const [showEleMenu, setShowEleMenu] = useState(false);

  useEffect(() => {
    dispatch(getAllDesigns())

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

      if (createdDes) history.push(`/designs/${createdDes.id}`);
    };
  };

  // LOADING TEMPLATES --------------------------------------------------
  let template;
  if (alias === 'presentation') {
    template = (
      <div
      style={{
        width:'960px',
        height:'540px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }
  if (alias === 'website') {
    template = (
      <div
      style={{
        width:'683px',
        height:'384px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }
  if (alias === 'resume') {
    template = (
      <div
      style={{
        width:'637.5px',
        height:'825px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }
  if (alias === 'igpost') {
    template = (
      <div
      style={{
        width:'480px',
        height:'480px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }
  if (alias === 'igstory') {
    template = (
      <div
      style={{
        width:'540px',
        height:'960px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }
  if (alias === 'fbpost') {
    template = (
      <div
      style={{
        width:'470px',
        height:'394px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }
  if (alias === 'invitation') {
    template = (
      <div
      style={{
        width:'375px',
        height:'525px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }
  if (alias === 'businesscard') {
    template = (
      <div
      style={{
        width:'336px',
        height:'192px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }
  if (alias === 'infograph') {
    template = (
      <div
      style={{
        width:'200px',
        height:'500px',
        backgroundColor:'white',
        boxShadow:'0px 8px 16px 0px rgba(0,0,0,0.2)',
      }}
      >
      </div>
    )
  }

  return (
    <div>
      {/* <div
          className='logo'
          onClick={() => window.location = '/designs'}
        >
          Home
        </div> */}
      <form className='create-des-form' onSubmit={handleSubmit}>
      {/* Create Design Form HERE */}
        <input
          id='des-name'
          type='text'
          placeholder="Design title"
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <button type='submit'>Save new design</button>
      </form>

      <div className="edit-container">
      <div className="sidebar">
        <button onClick={openSideMenu}>Templates</button>
        {showSideMenu && (
          <div id='temp-menu-item'>
            {templates.map(temp => (
              <div>
                {/* <img src={temp.alias}/> */}
                <button>{temp.name}</button>
              </div>
            ))}
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
    </div>
  )

}
