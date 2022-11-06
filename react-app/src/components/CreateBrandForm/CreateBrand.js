import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { createBrand } from "../../store/brands";

import './CreateBrand.css';

import { __colors } from "../../assets/colors";
import { __fonts } from "../../assets/fonts";

export default function CreateBrand() {
  const dispatch = useDispatch();
  const history = useHistory();

  const user = useSelector(state => state.session.user);
  const brands = useSelector(state => state.brands.allBrands);

  const [name, setName] = useState('');
  const [logo, setLogo] = useState('');
  const [colors, setColors] = useState([]);
  const [fonts, setFonts] = useState([]);

  const [validationErrs, setValidationErrs] = useState([]);
  const [hasSubmit, setHasSubmit] = useState(false);

  if (!user) {
    <h1>Please log in or create an account to create a brand.</h1>
  }

  useEffect(() => {
    const errs = [];

    if (!name.length) {
      errs.push('Please enter a brand name.')
    }
    if (name?.length && name.length < 2) {
      errs.push('Brand names must be at least 2 characters.')
    }
    if (name?.length && name.length > 25) {
      errs.push('This brand name is too long.')
    }
    // if (colors?.length && colors.length > 5) {
    //   errs.push('Too many colors selected. Please choose up to 5.')
    // }
    if(logo.length) {
      if (!logo.endsWith('.jpg') && !logo.endsWith('jpeg') && !logo.endsWith('.png')) {
        errs.push('Invalid logo url. Must end with ".jpg", ".jpeg", or ".png"')
      }
      if (!logo.startsWith('http://') && !logo.startsWith('https://')) {
        errs.push('Invalid logo url. Must start with "http://" or "https://"')
      }
    }
    if (errs.length) {
      setValidationErrs(errs);
    }
    else {
      setValidationErrs([]);
    }
  }, [name, logo]);

  const handleSubmit = async e => {
    e.preventDefault();

    setHasSubmit(true);

    const newBrand = {
      name,
      logo,
      colors,
      fonts
    }
    if (!validationErrs.length) {
      const createdBrand = await dispatch(createBrand(newBrand));

      if (createdBrand) history.push(`/brand/${createdBrand.id}`);
    };
  }

  return (
    <div>
      <h1 className="title">Create a brand</h1>
      <form className="brand-form" onSubmit={handleSubmit}>
        <div id='req'>
          * = required
        </div>
        <div className="input-errs">
          <div className="name-logo">
            <label id='brand-tag' for='brand-name-tag'>Brand name *</label>
            <input
              id='brand-name-tag'
              placeholder='Your brand here'
              type='text'
              value={name}
              onChange={e => setName(e.target.value)}
            />

            <label id='brand-tag' for='brand-logo'>Brand logo</label>
            <input
              id='brand-logo'
              type='text'
              value={logo}
              onChange={e => setLogo(e.target.value)}
              placeholder='image.url'
            />
          </div>

          {hasSubmit && validationErrs.length > 0 && (
            <div className='errors' id='br-err'>
              {validationErrs.map((error, idx) => (
                <div key={idx}>{error}</div>
              ))}
            </div>
          )}
        </div>
        <label id='brand-tag' for='brand-colors'>Brand colors:</label>
        <div className="color-container">
          {__colors.map(color => (
            <div id={color.alias} className='colors'>
              <input
                type='checkbox'
                id='brand-colors'
                value={color.alias}
                onChange={e => {
                  const colorList = colors;
                  if (e.target.checked) {
                    colorList.push(e.target.value)
                  }
                  else {
                    const i = colorList.indexOf(e.target.value);
                    colorList.splice(i, 1);
                  }
                  setColors(colorList)
                }}
              />
              <label
                for={color.alias}
                style={{
                  backgroundColor: `${color.alias}`,
                  color: `white`,
                  padding: '8px',
                  borderRadius: '3px',
                  textShadow: '#000 0 0 10px'
                }}>
                {color.alias}
              </label>
            </div>
          ))}
        </div>


        <label id='brand-tag' for='brand-fonts'>Brand fonts:</label>
        <div className="font-container">
          {__fonts.map(font => (
            <div id={font.family} className='fonts'>
              <input
                type='checkbox'
                id='brand-fonts'
                value={font.family}
                onChange={e => {
                  const fontList = fonts;
                  if (e.target.checked) {
                    fontList.push(e.target.value)
                  }
                  else {
                    const i = fontList.indexOf(e.target.value);
                    fontList.splice(i, 1);
                  }
                  setFonts(fontList)
                }}
              />
              <label
                for={font.family}
              // style={{
              //   fontFamily: `${font.family}`,
              //   color: `white`,
              //   padding: '8px',
              //   borderRadius: '3px',
              //   textShadow: '#000 0 0 10px'
              // }}
              >
                {font.family}
              </label>
            </div>
          ))}
        </div>

        <button id='brand-submit-button' type='submit'>Create new brand</button>
      </form>

    </div>
  )
}
