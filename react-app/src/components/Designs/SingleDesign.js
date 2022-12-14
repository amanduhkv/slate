import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory, useLocation } from "react-router-dom";
import { getADesign, updateDesign, clearData, getAllDesigns } from "../../store/designs";
import { getAllBrands } from "../../store/brands";
import './design.css';

import left from '../../icons/left.svg';
import outlinetemp from '../../icons/outline-temp.png';
import colors from '../../icons/colors.svg';
import fonts from '../../icons/fonts.svg';
// import present from '../../icons/temps/presentation.png';
// import website from '../../icons/temps/website.png';
// import resume from '../../icons/temps/resume.png';
// import igpost from '../../icons/temps/igpost.png';
// import igstory from '../../icons/temps/igstory.png';
// import fbpost from '../../icons/temps/fbpost.png';
// import inv from '../../icons/temps/invitation.png';
// import bizcard from '../../icons/temps/businesscard.png';
// import info from '../../icons/temps/infograph.png';
import DeleteDesign from "../DeleteDesignForm";

import pres1 from '../../icons/change-temps/present-temp/pres-original.svg';
import pres2 from '../../icons/change-temps/present-temp/pres-fun.svg';
import pres3 from '../../icons/change-temps/present-temp/pres-aesthetic.svg';
import pres4 from '../../icons/change-temps/present-temp/pres-green.svg';
import pres5 from '../../icons/change-temps/present-temp/pres-bw.svg';

import web1 from '../../icons/change-temps/website-temp/web-original.svg';
import web2 from '../../icons/change-temps/website-temp/web-fun.svg';
import web3 from '../../icons/change-temps/website-temp/web-aesthetic.svg';
import web4 from '../../icons/change-temps/website-temp/web-green.svg';
import web5 from '../../icons/change-temps/website-temp/web-bw.svg';

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

import { __colors, colorsByHue } from '../../assets/colors.js';
import { __fonts } from "../../assets/fonts";
import WebFont from 'webfontloader';

const TEMPLATES = {
  'presentation-original': pres1,
  'presentation-fun': pres2,
  'presentation-aesthetic': pres3,
  'presentation-green': pres4,
  'presentation-bw': pres5,
  'website-original': web1,
  'website-fun': web2,
  'website-aesthetic': web3,
  'website-green': web4,
  'website-bw': web5,
  'igpost-original': ig1,
  'igpost-fun': ig2,
  'igpost-aesthetic': ig3,
  'igpost-green': ig4,
  'igpost-bw': ig5,
  'igstory-original': igs1,
  'igstory-fun': igs2,
  'igstory-aesthetic': igs3,
  'igstory-green': igs4,
  'igstory-pink': igs5,
  'fbpost-original': fb1,
  'fbpost-fun': fb2,
  'fbpost-aesthetic': fb3,
  'fbpost-green': fb4,
  'fbpost-bw': fb5,
  'invitation-original': inv1,
  'invitation-fun': inv2,
  'invitation-aesthetic': inv3,
  'invitation-green': inv4,
  'invitation-bw': inv5,
  'businesscard-original': biz1,
  'businesscard-fun': biz2,
  'businesscard-aesthetic': biz3,
  'businesscard-green': biz4,
  'businesscard-bw': biz5,
  'infograph-original': info1,
  'infograph-fun': info2,
  'infograph-aesthetic': info3,
  'infograph-green': info4,
  'infograph-bw': info5,
  'resume-original': res1,
  'resume-fun': res2,
  'resume-aesthetic': res3,
  'resume-green': res4,
  'resume-bw': res5,
}

export default function SingleDesign() {
  const { designId } = useParams();
  const singleDesign = useSelector(state => state.designs.singleDesign);
  // console.log('This is the single design deets', singleDesign)
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
  const [showFontMenu, setShowFontMenu] = useState(false);
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  // const [input3, setInput3] = useState('');
  // const [input4, setInput4] = useState('');
  // const [input5, setInput5] = useState('');
  const [color, setColor] = useState('');
  const [font, setFont] = useState('');
  const [background, setBackground] = useState('');

  // console.log('current font is', font)
    WebFont.load({
      google: {
        families: [font]
      }
    });


  if (!Object.values(singleDesign).length) {
    dispatch(getADesign(designId))
  }

  // set to top of page on render
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [window])

  // dispatches
  useEffect(() => {
    dispatch(getADesign(designId))
    dispatch(getAllDesigns());
    dispatch(getAllBrands());

    return () => dispatch(clearData())
  }, [dispatch, designId])


  // SIDEBAR MENU FXNS ---------------------------------------------
  //template ===========
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

  //brand ============
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

  //font ============
  const openFontMenu = () => {
    if (showBrandMenu) return;
    setShowFontMenu(true);
  };

  useEffect(() => {
    if (!showFontMenu) return;
    const closeFontMenu = () => {
      setShowFontMenu(false);
    };
    document.addEventListener('click', closeFontMenu);
    return () => document.removeEventListener("click", closeFontMenu);
  }, [showFontMenu]);

  // LOADING PREV DATA ---------------------------------------
  useEffect(() => {
    if (singleDesign) {
      setName(singleDesign.name)
      setTemp(singleDesign.background ? singleDesign.background : alias)
      setBackground(singleDesign.background ? singleDesign.background : alias)
      setFont(singleDesign.font ? singleDesign.font : '')
      setColor(singleDesign.color ? singleDesign.color : '')
      setInput1(singleDesign.text_input_1 ? singleDesign.text_input_1 : '')
      setInput2(singleDesign.text_input_2 ? singleDesign.text_input_2 : '')
    }
  }, [singleDesign, alias])

  // SUBMIT FXNS ---------------------------------------------
  useEffect(() => {
    const errors = [];

    if (!name?.length) {
      errors.push('Please confirm these changes by re-entering the name for this design, or entering a new name for the design.')
    }

    setValidationErrs(errors);
  }, [name]);


  // CHANGING BCKGD COLOR FXNS ------------------------------------------
  // useEffect(() => {
  //   if(singleDesign.color) {
  //     setBackground(singleDesign.color)
  //   }
  // }, [singleDesign.color])

  // ADDING ANOTHER PAGE ------------------------------------------------
  // const addPage = () => {
  //   const page = document.getElementById('adding-another');
  //   page.innerHTML = template;
  // }

  // LOADING TEMPLATES --------------------------------------------------
  let template;

  // console.log('CURRENT alias', alias)
  // console.log('CURRENT Background', background)
  // console.log('CURRENT SINGLEDES.BG', singleDesign.background)
  // console.log('SINGLE DES', singleDesign)

  if (background.includes('presentation')) {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: (background.includes('original') ? `center / contain url(${pres1}) ${color}` :
            background.includes('fun') ? `center / contain url(${pres2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${pres3}) ${color}` :
                background.includes('green') ? `center / contain url(${pres4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${pres5}) ${color}` :
                    background)
        }}
      >
        {background.includes('original') || background.includes('fun') || background.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                fontFamily: `${font}`,
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '880px',
                height: '440px',
                maxWidth: '880px',
                maxHeight: '440px',
                minWidth: '347px',
                minHeight: '120px'
              }}
            />
          </div> : background.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  resize: 'none',
                  height: '295px',
                  width: '400px'
                }}
              />
            </div> : background.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    marginLeft: '120px'
                  }}
                />
                <textarea
                  id='input2'
                  value={input2}
                  placeholder="Your text here"
                  onChange={(e) => setInput2(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '680px',
                    height: '440px',
                    maxWidth: '680px',
                    maxHeight: '440px',
                    minWidth: '347px',
                    minHeight: '120px',
                    marginLeft: '120px'
                  }}
                />
              </div> : null
        }
      </div>
    )
  }
  if (background.includes('website')) {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: background.includes('original') ? `center / contain url(${web1}) ${color}` :
            background.includes('fun') ? `center / contain url(${web2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${web3}) ${color}` :
                background.includes('green') ? `center / contain url(${web4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${web5}) ${color}` :
                    background
        }}
      >
        {background.includes('original') || background.includes('fun') || background.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                fontFamily: `${font}`,
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '580px',
                height: '240px',
                maxWidth: '580px',
                maxHeight: '240px',
                minWidth: '347px',
                minHeight: '120px'
              }}
            />
          </div> : background.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '200px',
                  height: '27px',
                  marginTop: '8px',
                  marginLeft: '276px',
                  fontSize: '20px'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '210px',
                  height: '240px',
                  resize: 'none',
                  maxWidth: '210px',
                  maxHeight: '240px',
                  // minWidth: '347px',
                  minHeight: '120px',
                  marginLeft: '270px'
                }}
              />
            </div> : background.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    marginLeft: '310px'
                  }}
                />
                <textarea
                  id='input2'
                  value={input2}
                  placeholder="Your text here"
                  onChange={(e) => setInput2(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '350px',
                    height: '280px',
                    marginTop: '8px',
                    marginLeft: '310px',
                    resize: 'none'
                  }}
                />
              </div> : null
        }
      </div>
    )
  }
  if (background.includes('resume')) {
    template = (
      <div
        className="template"
        style={{
          width: '425px',
          height: '550px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: (background.includes('original') ? `center / contain url(${res1}) ${color}` :
            background.includes('fun') ? `center / contain url(${res2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${res3}) ${color}` :
                background.includes('green') ? `center / contain url(${res4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${res5}) ${color}` :
                    background)
        }}
      >
        {background.includes('original') || background.includes('fun') || background.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                fontFamily: `${font}`,
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '370px',
                height: '430px',
                marginTop: '8px',
                resize: 'none'
              }}
            />
          </div> : background.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '235px',
                  height: '40px',
                  marginTop: '68px',
                  marginRight: '122px',
                  resize: 'none'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '165px',
                  height: '280px',
                  marginTop: '88px',
                  marginRight: '122px',
                  resize: 'none'
                }}
              />
            </div> : background.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '270px',
                    marginTop: '8px',
                    marginLeft: '80px',
                    resize: 'none'
                  }}
                />
                <textarea
                  id='input2'
                  value={input2}
                  placeholder="Your text here"
                  onChange={(e) => setInput2(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '270px',
                    height: '430px',
                    marginTop: '8px',
                    marginLeft: '80px',
                    resize: 'none'
                  }}
                />
              </div> : null
        }
      </div>
    )
  }
  if (background.includes('igpost')) {
    template = (
      <div
        className="template"
        style={{
          width: '480px',
          height: '480px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: (background.includes('original') ? `center / contain url(${ig1}) ${color}` :
            background.includes('fun') ? `center / contain url(${ig2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${ig3}) ${color}` :
                background.includes('green') ? `center / contain url(${ig4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${ig5}) ${color}` :
                    background)
        }}
      >
        {background.includes('original') || background.includes('fun') || background.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                fontFamily: `${font}`,
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '406px',
                height: '346px',
                marginTop: '8px',
                resize: 'none'
              }}
            />
          </div> : background.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  marginTop: '180px'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '406px',
                  height: '146px',
                  marginTop: '8px',
                  resize: 'none'
                }}
              />
            </div> : background.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '246px',
                    marginLeft: '190px',
                  }}
                />
                <textarea
                  id='input2'
                  value={input2}
                  placeholder="Your text here"
                  onChange={(e) => setInput2(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '246px',
                    height: '346px',
                    marginTop: '8px',
                    marginLeft: '190px',
                    resize: 'none'
                  }}
                />
              </div> : null
        }
      </div>
    )
  }
  if (background.includes('igstory')) {
    template = (
      <div
        className="template"
        style={{
          width: '270px',
          height: '480px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: (background.includes('original') ? `center / contain url(${igs1}) ${color}` :
            background.includes('fun') ? `center / contain url(${igs2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${igs3}) ${color}` :
                background.includes('green') ? `center / contain url(${igs4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${igs5}) ${color}` :
                    background)
        }}
      >
        {background.includes('original') || background.includes('fun') || background.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '230px'
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '230px',
                height: '346px',
                resize: 'none'
              }}
            />
          </div> : background.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '200px',
                  marginTop: '40px'
                }}
              />
            </div> : background.includes('pink') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '200px',
                    marginBottom: '40px',
                    marginLeft: '24px',
                    transform: 'rotate(4deg)'
                  }}
                />
              </div> : null
        }
      </div>
    )
  }
  if (background.includes('fbpost')) {
    template = (
      <div
        className="template"
        style={{
          width: '470px',
          height: '394px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: (background.includes('original') ? `center / contain url(${fb1}) ${color}` :
            background.includes('fun') ? `center / contain url(${fb2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${fb3}) ${color}` :
                background.includes('green') ? `center / contain url(${fb4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${fb5}) ${color}` :
                    background)
        }}
      >
        {background.includes('original') || background.includes('fun') || background.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                fontFamily: `${font}`,
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '430px',
                height: '290px',
                resize: 'none'
              }}
            />
          </div> : background.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  marginTop: '180px'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '430px',
                  height: '150px',
                  resize: 'none'
                }}
              />
            </div> : background.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    marginBottom: '235px'
                  }}
                />
              </div> : null
        }
      </div>
    )
  }
  if (background.includes('invitation')) {
    template = (
      <div
        className="template"
        style={{
          width: '375px',
          height: '525px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: (background.includes('original') ? `center / contain url(${inv1}) ${color}` :
            background.includes('fun') ? `center / contain url(${inv2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${inv3}) ${color}` :
                background.includes('green') ? `center / contain url(${inv4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${inv5}) ${color}` :
                    background)
        }}
      >
        {background.includes('original') || background.includes('fun') || background.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                fontFamily: `${font}`,
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '350px',
                height: '425px',
                resize: 'none'
              }}
            />
          </div> : background.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  marginTop: '230px'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '344px',
                  height: '188px',
                  resize: 'none'
                }}
              />
            </div> : background.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '270px',
                    height: '45px',
                    resize: 'none',
                    marginTop: '15px',
                    marginLeft: '80px'
                  }}
                />
                <textarea
                  id='input2'
                  value={input2}
                  placeholder="Your text here"
                  onChange={(e) => setInput2(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '270px',
                    height: '225px',
                    resize: 'none',
                    marginTop: '210px',
                    marginLeft: '80px'
                  }}
                />
              </div> : null
        }
      </div>
    )
  }
  if (background.includes('businesscard')) {
    template = (
      <div
        className="template"
        style={{
          width: '336px',
          height: '192px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: (background.includes('original') ? `center / contain url(${biz1}) ${color}` :
            background.includes('fun') ? `center / contain url(${biz2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${biz3}) ${color}` :
                background.includes('green') ? `center / contain url(${biz4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${biz5}) ${color}` :
                    background)
        }}
      >
        {background.includes('original') || background.includes('fun') || background.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '280px',
                marginLeft: '8px'
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                fontFamily: `${font}`,
                width: '280px',
                height: '72px',
                resize: 'none',
                marginLeft: '8px'
              }}
            />
          </div> : background.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '160px',
                  marginLeft: '140px',
                  marginTop: '65px'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  fontFamily: `${font}`,
                  width: '160px',
                  height: '62px',
                  resize: 'none',
                  marginLeft: '140px',
                  marginTop: '-5px'
                }}
              />
            </div> : background.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '190px',
                    marginLeft: '130px',
                    marginTop: '65px'
                  }}
                />
                <textarea
                  id='input2'
                  value={input2}
                  placeholder="Your text here"
                  onChange={(e) => setInput2(e.target.value)}
                  style={{
                    fontFamily: `${font}`,
                    width: '190px',
                    height: '62px',
                    resize: 'none',
                    marginLeft: '130px',
                    marginTop: '-5px'
                  }}
                />
              </div> : null
        }

      </div>
    )
  }
  if (background.includes('infograph')) {
    template = (
      <div
        className="template"
        style={{
          width: '200px',
          height: '500px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: (background.includes('original') ? `center / contain url(${info1}) ${color}` :
            background.includes('fun') ? `center / contain url(${info2}) ${color}` :
              background.includes('aesthetic') ? `center / contain url(${info3}) ${color}` :
                background.includes('green') ? `center / contain url(${info4}) ${color}` :
                  background.includes('bw') ? `center / contain url(${info5}) ${color}` :
                    background)
        }}
      >
        <div id='template-inputs'>
          <input
            id='input1'
            type='text'
            placeholder="Title Here"
            value={input1}
            onChange={(e) => setInput1(e.target.value)}
            style={{
              fontFamily: `${font}`,
              width: '150px'
            }}
          />
          <textarea
            id='input2'
            value={input2}
            placeholder="Your text here"
            onChange={(e) => setInput2(e.target.value)}
            style={{
              fontFamily: `${font}`,
              width: '150px',
              height: '400px',
              maxWidth: '150px',
              minWidth: '150px',
              maxHeight: '400px',
              minHeight: '150px'
            }}
          />
        </div>
      </div>
    )
  }




  const handleSubmit = async e => {
    e.preventDefault();

    setHasSubmit(true);
    // console.log('THIS IS BG BEFORE PAYLOAD', background)
    const payload = {
      name: name,
      template: alias,
      background: background,
      color: color,
      font: font,
      text_input_1: input1,
      text_input_2: input2,
    };
    // console.log('PAYLOAD', payload)
    if (!validationErrs.length) {
      let updatedDes = await dispatch(updateDesign(singleDesign.id, payload));
      // console.log('updatedDes', updatedDes)

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
          {user && user.id !== singleDesign.user_id && (
            <h2 style={{ margin: '0' }}>
              {singleDesign.name}
            </h2>
          )}
          {user && user.id === singleDesign.user_id && (
            <>
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
                onChange={e => {
                  setTemp(e.target.value)
                }}
              />
              <input
                type='text'
                value={background}
                hidden
                onChange={e => {
                  setBackground(e.target.value)
                }}
              />
              <input
                type='text'
                value={color}
                hidden
                onChange={e => {
                  setColor(e.target.value)
                }}
              />
              <input
                type='text'
                value={font}
                hidden
                onChange={e => {
                  setFont(e.target.value)
                }}
              />
              <textarea
                hidden
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
              />
              <textarea
                hidden
                value={input2}
                onChange={(e) => setInput2(e.target.value)}
              />
              <button id='create-des-button' type='submit'>Save design</button>
              <DeleteDesign />
            </>
          )}
        </div>
      </form>

      <div className="edit-container">
        {user && user.id === singleDesign.user_id && (
          <div className="sidebar">
            <button id='sidebar' onClick={openSideMenu}>
              <img src={outlinetemp} alt='temp' height='40px' />
              Templates
            </button>
            {showSideMenu && (
              <div className="temp-menu-container">
                {/* <div id='warning'>Warning: Switching templates deletes any previous work made.</div> */}
                <div id='temp-menu-item'>
                  {allDesigns[1].template.map(temp => (
                    <div id='temp-container-des' onClick={() => {
                      setTemp(temp.alias)
                      setBackground(temp.alias)
                      const image = document.getElementById('temp-img')
                      image.src = TEMPLATES[temp.alias]
                    }}>
                      {temp.alias === 'presentation-original' ?
                        <img id='temp-img' src={pres1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                        temp.alias === 'presentation-fun' ?
                          <img id='temp-img' src={pres2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                          temp.alias === 'presentation-aesthetic' ?
                            <img id='temp-img' src={pres3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                            temp.alias === 'presentation-green' ?
                              <img id='temp-img' src={pres4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                              temp.alias === 'presentation-bw' ?
                                <img id='temp-img' src={pres5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                temp.alias === 'website-original' ?
                                  <img id='temp-img' src={web1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                  temp.alias === 'website-fun' ?
                                    <img id='temp-img' src={web2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                    temp.alias === 'website-aesthetic' ?
                                      <img id='temp-img' src={web3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                      temp.alias === 'website-green' ?
                                        <img id='temp-img' src={web4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                        temp.alias === 'website-bw' ?
                                          <img id='temp-img' src={web5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                          temp.alias === 'resume-original' ?
                                            <img id='temp-img' src={res1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                            temp.alias === 'resume-fun' ?
                                              <img id='temp-img' src={res2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                              temp.alias === 'resume-aesthetic' ?
                                                <img id='temp-img' src={res3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                temp.alias === 'resume-green' ?
                                                  <img id='temp-img' src={res4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                  temp.alias === 'resume-bw' ?
                                                    <img id='temp-img' src={res5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                    temp.alias === 'igpost-original' ?
                                                      <img id='temp-img' src={ig1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                      temp.alias === 'igpost-fun' ?
                                                        <img id='temp-img' src={ig2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                        temp.alias === 'igpost-aesthetic' ?
                                                          <img id='temp-img' src={ig3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                          temp.alias === 'igpost-green' ?
                                                            <img id='temp-img' src={ig4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                            temp.alias === 'igpost-bw' ?
                                                              <img id='temp-img' src={ig5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                              temp.alias === 'igstory-original' ?
                                                                <img id='temp-img' src={igs1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                temp.alias === 'igstory-fun' ?
                                                                  <img id='temp-img' src={igs2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                  temp.alias === 'igstory-aesthetic' ?
                                                                    <img id='temp-img' src={igs3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                    temp.alias === 'igstory-green' ?
                                                                      <img id='temp-img' src={igs4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                      temp.alias === 'igstory-pink' ?
                                                                        <img id='temp-img' src={igs5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                        temp.alias === 'fbpost-original' ?
                                                                          <img id='temp-img' src={fb1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                          temp.alias === 'fbpost-fun' ?
                                                                            <img id='temp-img' src={fb2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                            temp.alias === 'fbpost-aesthetic' ?
                                                                              <img id='temp-img' src={fb3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                              temp.alias === 'fbpost-green' ?
                                                                                <img id='temp-img' src={fb4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                temp.alias === 'fbpost-bw' ?
                                                                                  <img id='temp-img' src={fb5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                  temp.alias === 'invitation-original' ?
                                                                                    <img id='temp-img' src={inv1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                    temp.alias === 'invitation-fun' ?
                                                                                      <img id='temp-img' src={inv2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                      temp.alias === 'invitation-aesthetic' ?
                                                                                        <img id='temp-img' src={inv3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                        temp.alias === 'invitation-green' ?
                                                                                          <img id='temp-img' src={inv4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                          temp.alias === 'invitation-bw' ?
                                                                                            <img id='temp-img' src={inv5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                            temp.alias === 'businesscard-original' ?
                                                                                              <img id='temp-img' src={biz1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                              temp.alias === 'businesscard-fun' ?
                                                                                                <img id='temp-img' src={biz2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                temp.alias === 'businesscard-aesthetic' ?
                                                                                                  <img id='temp-img' src={biz3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                  temp.alias === 'businesscard-green' ?
                                                                                                    <img id='temp-img' src={biz4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                    temp.alias === 'businesscard-bw' ?
                                                                                                      <img id='temp-img' src={biz5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                      temp.alias === 'infograph-original' ?
                                                                                                        <img id='temp-img' src={info1} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                        temp.alias === 'infograph-fun' ?
                                                                                                          <img id='temp-img' src={info2} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                          temp.alias === 'infograph-aesthetic' ?
                                                                                                            <img id='temp-img' src={info3} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                            temp.alias === 'infograph-green' ?
                                                                                                              <img id='temp-img' src={info4} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                              temp.alias === 'infograph-bw' ?
                                                                                                                <img id='temp-img' src={info5} alt='pres' width='160px' style={{background: 'rgb(242,243,245)'}} /> :
                                                                                                                "Your template here"
                      }
                      <button id='create-des-temp-button'>{temp.name}</button>
                    </div>
                  ))}

                </div>

              </div>
            )}


            <button id='sidebar' onClick={openBrandMenu}>
              <img src={colors} alt='temp' height='40px' />
              Background Colors
            </button>
            {showBrandMenu && (
              <div id='temp-menu-item'>
                <div className='brands-menu-item'>
                  <div id='temp-brand-title'>
                    Brands
                  </div>
                  <div className="colors-container">
                    {Object.values(brands).map(brand => (
                      <div className="des-brand-colors">
                        <div id='des-brand-name'>
                          {brand.name}
                        </div>
                        <div id='brand-color-container'>
                        {brand.colors.map(color => (
                          <div
                            id='each-color'
                            onClick={() => {
                              setColor(color.name);
                            }}
                            style={{
                              backgroundColor: `${color.name}`
                            }}
                          >
                            {/* {color.name} */}
                          </div>
                        ))}
                        </div>
                        {/* {brand.fonts.map(font => (
                      <div
                        onClick={() => setFont(font.name)}
                      >
                        {font.name}
                      </div>
                    ))} */}
                      </div>
                    ))}
                  </div>
                </div>
                <div className='brands-menu-item'>
                  <div id='color-title'>
                    Colors
                  </div>
                  <div className='color-container'>
                    {colorsByHue.map(color => (
                      <div
                      id='each-color'
                      onClick={() => {
                        setColor(color.alias);
                      }}
                      style={{
                        backgroundColor: `${color.alias}`
                      }}
                    >
                      {/* {color.name} */}
                    </div>
                    ))}
                  </div>
                </div>
              </div>
            )}
            <button id='sidebar' onClick={openFontMenu}>
              <img src={fonts} alt='temp' height='34px' />
              Fonts
            </button>
            {showFontMenu && (
              <div id='temp-menu-item'>
                {/* {singleDesign.font} */}
                {__fonts.map(font => (
                  <div
                    id='each-font'
                    onClick={() => {
                      setFont(font.family)
                    }}
                    style={{
                      // fontFamily: `Poppins`,
                      fontSize: '18px'
                    }}
                  >
                    {font.family}
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
        <div className="edit-area">
          {user && user.id === singleDesign.user_id && (
            <>
              <div id='top-menu'>
                <button
                  id='tm-font'
                  onClick={() => {
                    openFontMenu()
                  }}
                >
                  {singleDesign.font}
                </button>
                <button
                  className='tm-font-button'
                  onClick={() => {
                    if (document.getElementById('input1').style.fontWeight === '700') {
                      document.getElementById('input1').style.fontWeight = '400'
                    } else {
                      document.getElementById('input1').style.fontWeight = '700'
                    }

                    if (document.getElementById('input2').style.fontWeight === '700') {
                      document.getElementById('input2').style.fontWeight = '400'
                    } else {
                      document.getElementById('input2').style.fontWeight = '700'
                    }

                  }}
                >
                  B
                </button>
                {/* <button
                  className='tm-font-button'
                >
                  I
                </button>
                <div>|</div>
                <button
                  className='tm-font-button'
                  id='effects'
                >
                  Effects
                </button> */}
              </div>
              <div id="inserted-temp">
                {template}
              </div>
              {/* <button id='add-page'
              onClick={() => {
                const page = document.getElementById('adding-another');
                page.innerHTML = {template};
              }}
              >
                +
              </button> */}
            </>
          )}
          {user && user.id !== singleDesign.user_id && (
            <div id="inserted-temp" style={{ pointerEvents: 'none' }}>
              {template}
            </div>
          )}
        </div>
      </div>
      {/* {template} */}
    </div>
  )
}
