import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory, useLocation } from "react-router-dom";
import { getADesign, updateDesign, clearData, getAllDesigns } from "../../store/designs";
import { getAllBrands } from "../../store/brands"

import left from '../../icons/left.svg';
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
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  // const [input3, setInput3] = useState('');
  // const [input4, setInput4] = useState('');
  // const [input5, setInput5] = useState('');
  const [color, setColor] = useState('');
  const [font, setFont] = useState('');

  const [background, setBackground] = useState('');
  // const [currFont, setCurrFont] = useState('');
  if (!Object.values(singleDesign).length) {
    dispatch(getADesign(designId))
  }

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

  // LOADING PREV DATA ---------------------------------------
  useEffect(() => {
    if (singleDesign) {
      setName(singleDesign.name)
      if (alias) {
        setTemp(alias)
      }
      setBackground(singleDesign.background ?? '')
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
  // if (singleDesign.color) {
  //   setBackground(singleDesign.color)
  // }
  // useEffect(() => {
  //   const resultingTemp = document.getElementsByClassName('template')[0];
  //   console.log('RESULTING TEMPS', resultingTemp);
  //   if(singleDesign) {
  //     resultingTemp.style['background-color'] = backgroundColor
  //   }
  // }, [backgroundColor])

  // LOADING TEMPLATES --------------------------------------------------
  let template;

  console.log('CURRENT alias', alias)
  console.log('CURRENT Background', background)
  console.log('CURRENT SINGLEDES.BG', singleDesign.background)
  console.log('SINGLE DES', singleDesign)

  if (alias.includes('presentation')) {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          // backgroundColor: 'white',
          background: (background.includes('original') ? `url(${pres1})` :
          background.includes('fun') ? `url(${pres2})` :
            background.includes('aesthetic') ? `url(${pres3})` :
              background.includes('green') ? `url(${pres4})` :
                background.includes('bw') ? `url(${pres5})` :
                  background)
          // `url(${alias.includes('original') ? pres1 :
          //   alias.includes('fun') ? pres2 :
          //     alias.includes('aesthetic') ? pres3 :
          //       alias.includes('green') ? pres4 :
          //         alias.includes('bw') ? pres5 :
          //           null
          //   })`
        }}
      >
        {alias.includes('original') || alias.includes('fun') || alias.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                // fontFamily: `${singleDesign.font} ? ${singleDesign.font} : "Noto Sans"`,
                color: `${singleDesign.color}`
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                width: '880px',
                height: '440px',
                maxWidth: '880px',
                maxHeight: '440px',
                minWidth: '347px',
                minHeight: '120px'
              }}
            />
          </div> : alias.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  resize: 'none',
                  height: '295px',
                  width: '400px'
                }}
              />
            </div> : alias.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    marginLeft: '120px'
                  }}
                />
                <textarea
                  id='input2'
                  value={input2}
                  placeholder="Your text here"
                  onChange={(e) => setInput2(e.target.value)}
                  style={{
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
  if (alias.includes('website')) {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
          background: `${background}`,
          backgroundImage: `url(${alias.includes('original') ? web1 :
            alias.includes('fun') ? web2 :
              alias.includes('aesthetic') ? web3 :
                alias.includes('green') ? web4 :
                  alias.includes('bw') ? web5 :
                    null
            })`
        }}
      >
        {alias.includes('original') || alias.includes('fun') || alias.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                width: '580px',
                height: '240px',
                maxWidth: '580px',
                maxHeight: '240px',
                minWidth: '347px',
                minHeight: '120px'
              }}
            />
          </div> : alias.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
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
            </div> : alias.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    marginLeft: '310px'
                  }}
                />
                <textarea
                  id='input2'
                  value={input2}
                  placeholder="Your text here"
                  onChange={(e) => setInput2(e.target.value)}
                  style={{
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
  if (alias.includes('resume')) {
    template = (
      <div
        className="template"
        style={{
          width: '425px',
          height: '550px',
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
        {alias.includes('original') || alias.includes('fun') || alias.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                width: '370px',
                height: '430px',
                marginTop: '8px',
                resize: 'none'
              }}
            />
          </div> : alias.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
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
                  width: '165px',
                  height: '280px',
                  marginTop: '88px',
                  marginRight: '122px',
                  resize: 'none'
                }}
              />
            </div> : alias.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
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
        {alias.includes('original') || alias.includes('fun') || alias.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                width: '406px',
                height: '346px',
                marginTop: '8px',
                resize: 'none'
              }}
            />
          </div> : alias.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  marginTop: '180px'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  width: '406px',
                  height: '146px',
                  marginTop: '8px',
                  resize: 'none'
                }}
              />
            </div> : alias.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
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
        {alias.includes('original') || alias.includes('fun') || alias.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
                width: '230px'
              }}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                width: '230px',
                height: '346px',
                resize: 'none'
              }}
            />
          </div> : alias.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  width: '200px',
                  marginTop: '40px'
                }}
              />
            </div> : alias.includes('pink') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
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
        {alias.includes('original') || alias.includes('fun') || alias.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                width: '430px',
                height: '290px',
                resize: 'none'
              }}
            />
          </div> : alias.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  marginTop: '180px'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  width: '430px',
                  height: '150px',
                  resize: 'none'
                }}
              />
            </div> : alias.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
                    marginBottom: '235px'
                  }}
                />
              </div> : null
        }
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
        {alias.includes('original') || alias.includes('fun') || alias.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
            />
            <textarea
              id='input2'
              value={input2}
              placeholder="Your text here"
              onChange={(e) => setInput2(e.target.value)}
              style={{
                width: '350px',
                height: '425px',
                resize: 'none'
              }}
            />
          </div> : alias.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
                  marginTop: '230px'
                }}
              />
              <textarea
                id='input2'
                value={input2}
                placeholder="Your text here"
                onChange={(e) => setInput2(e.target.value)}
                style={{
                  width: '344px',
                  height: '188px',
                  resize: 'none'
                }}
              />
            </div> : alias.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
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
        {alias.includes('original') || alias.includes('fun') || alias.includes('aesthetic') ?
          <div id='template-inputs'>
            <input
              id='input1'
              type='text'
              placeholder="Title Here"
              value={input1}
              onChange={(e) => setInput1(e.target.value)}
              style={{
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
                width: '280px',
                height: '72px',
                resize: 'none',
                marginLeft: '8px'
              }}
            />
          </div> : alias.includes('green') ?
            <div id='template-inputs'>
              <input
                id='input1'
                type='text'
                placeholder="Title Here"
                value={input1}
                onChange={(e) => setInput1(e.target.value)}
                style={{
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
                  width: '160px',
                  height: '62px',
                  resize: 'none',
                  marginLeft: '140px',
                  marginTop: '-5px'
                }}
              />
            </div> : alias.includes('bw') ?
              <div id='template-inputs'>
                <input
                  id='input1'
                  type='text'
                  placeholder="Title Here"
                  value={input1}
                  onChange={(e) => setInput1(e.target.value)}
                  style={{
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
        <div id='template-inputs'>
          <input
            id='input1'
            type='text'
            placeholder="Title Here"
            value={input1}
            onChange={(e) => setInput1(e.target.value)}
            style={{
              width: '150px'
            }}
          />
          <textarea
            id='input2'
            value={input2}
            placeholder="Your text here"
            onChange={(e) => setInput2(e.target.value)}
            style={{
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
    console.log('THIS IS BG BEFORE PAYLOAD', background)
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
                // hidden
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
            <button onClick={openSideMenu}>Templates</button>
            {showSideMenu && (
              <div className="temp-menu-container">
                {/* <div id='warning'>Warning: Switching templates deletes any previous work made.</div> */}
                <div id='temp-menu-item'>
                  {allDesigns[1].template.map(temp => (
                    <div id='temp-container-des' onClick={() => {
                      setTemp(temp.alias)
                      setBackground(temp.alias)
                      history.push(`/designs/${designId}/${temp.alias}`)
                    }}>
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
                                          temp.alias === 'resume-original' ?
                                            <img id='temp-img' src={res1} alt='pres' width='160px' /> :
                                            temp.alias === 'resume-fun' ?
                                              <img id='temp-img' src={res2} alt='pres' width='160px' /> :
                                              temp.alias === 'resume-aesthetic' ?
                                                <img id='temp-img' src={res3} alt='pres' width='160px' /> :
                                                temp.alias === 'resume-green' ?
                                                  <img id='temp-img' src={res4} alt='pres' width='160px' /> :
                                                  temp.alias === 'resume-bw' ?
                                                    <img id='temp-img' src={res5} alt='pres' width='160px' /> :
                                                    temp.alias === 'igpost-original' ?
                                                      <img id='temp-img' src={ig1} alt='pres' width='160px' /> :
                                                      temp.alias === 'igpost-fun' ?
                                                        <img id='temp-img' src={ig2} alt='pres' width='160px' /> :
                                                        temp.alias === 'igpost-aesthetic' ?
                                                          <img id='temp-img' src={ig3} alt='pres' width='160px' /> :
                                                          temp.alias === 'igpost-green' ?
                                                            <img id='temp-img' src={ig4} alt='pres' width='160px' /> :
                                                            temp.alias === 'igpost-bw' ?
                                                              <img id='temp-img' src={ig5} alt='pres' width='160px' /> :
                                                              temp.alias === 'igstory-original' ?
                                                                <img id='temp-img' src={igs1} alt='pres' width='160px' /> :
                                                                temp.alias === 'igstory-fun' ?
                                                                  <img id='temp-img' src={igs2} alt='pres' width='160px' /> :
                                                                  temp.alias === 'igstory-aesthetic' ?
                                                                    <img id='temp-img' src={igs3} alt='pres' width='160px' /> :
                                                                    temp.alias === 'igstory-green' ?
                                                                      <img id='temp-img' src={igs4} alt='pres' width='160px' /> :
                                                                      temp.alias === 'igstory-pink' ?
                                                                        <img id='temp-img' src={igs5} alt='pres' width='160px' /> :
                                                                        temp.alias === 'fbpost-original' ?
                                                                          <img id='temp-img' src={fb1} alt='pres' width='160px' /> :
                                                                          temp.alias === 'fbpost-fun' ?
                                                                            <img id='temp-img' src={fb2} alt='pres' width='160px' /> :
                                                                            temp.alias === 'fbpost-aesthetic' ?
                                                                              <img id='temp-img' src={fb3} alt='pres' width='160px' /> :
                                                                              temp.alias === 'fbpost-green' ?
                                                                                <img id='temp-img' src={fb4} alt='pres' width='160px' /> :
                                                                                temp.alias === 'fbpost-bw' ?
                                                                                  <img id='temp-img' src={fb5} alt='pres' width='160px' /> :
                                                                                  temp.alias === 'invitation-original' ?
                                                                                    <img id='temp-img' src={inv1} alt='pres' width='160px' /> :
                                                                                    temp.alias === 'invitation-fun' ?
                                                                                      <img id='temp-img' src={inv2} alt='pres' width='160px' /> :
                                                                                      temp.alias === 'invitation-aesthetic' ?
                                                                                        <img id='temp-img' src={inv3} alt='pres' width='160px' /> :
                                                                                        temp.alias === 'invitation-green' ?
                                                                                          <img id='temp-img' src={inv4} alt='pres' width='160px' /> :
                                                                                          temp.alias === 'invitation-bw' ?
                                                                                            <img id='temp-img' src={inv5} alt='pres' width='160px' /> :
                                                                                            temp.alias === 'businesscard-original' ?
                                                                                              <img id='temp-img' src={biz1} alt='pres' width='160px' /> :
                                                                                              temp.alias === 'businesscard-fun' ?
                                                                                                <img id='temp-img' src={biz2} alt='pres' width='160px' /> :
                                                                                                temp.alias === 'businesscard-aesthetic' ?
                                                                                                  <img id='temp-img' src={biz3} alt='pres' width='160px' /> :
                                                                                                  temp.alias === 'businesscard-green' ?
                                                                                                    <img id='temp-img' src={biz4} alt='pres' width='160px' /> :
                                                                                                    temp.alias === 'businesscard-bw' ?
                                                                                                      <img id='temp-img' src={biz5} alt='pres' width='160px' /> :
                                                                                                      temp.alias === 'infograph-original' ?
                                                                                                        <img id='temp-img' src={info1} alt='pres' width='160px' /> :
                                                                                                        temp.alias === 'infograph-fun' ?
                                                                                                          <img id='temp-img' src={info2} alt='pres' width='160px' /> :
                                                                                                          temp.alias === 'infograph-aesthetic' ?
                                                                                                            <img id='temp-img' src={info3} alt='pres' width='160px' /> :
                                                                                                            temp.alias === 'infograph-green' ?
                                                                                                              <img id='temp-img' src={info4} alt='pres' width='160px' /> :
                                                                                                              temp.alias === 'infograph-bw' ?
                                                                                                                <img id='temp-img' src={info5} alt='pres' width='160px' /> :
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
              // <div id='temp-menu-item-brand'>
              //   <div id='brand-side-content'>Oops! Looks like this feature is still in the works. In the meantime, try checking out brands for the future!

              //     <button
              //       onClick={() => history.push('/brand')}
              //     >Go to brands</button>
              //   </div>
              // </div>
              <div id='temp-menu-item'>
                {Object.values(brands).map(brand => (
                  <div className="des-brand-colors">
                    {brand.colors.map(color => (
                      <div
                        id='each-color'
                        onClick={() => {
                          setColor(color.name);
                          setBackground(color.name)
                          // localStorage.setItem('backgroundColor', color.name)
                        }}
                        style={{
                          backgroundColor: `${color.name}`
                        }}
                      >
                        {/* {color.name} */}
                      </div>
                    ))}
                    {brand.fonts.map(font => (
                      <div
                        onClick={() => setFont(font.name)}
                      >
                        {font.name}
                      </div>
                    ))}
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
        <div className="edit-area">
          {user && user.id === singleDesign.user_id && (
            <div id="inserted-temp">
              {template}
            </div>
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
