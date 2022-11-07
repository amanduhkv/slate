import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import { createDesign, getAllDesigns, clearData } from "../../store/designs";

import './CreateDesignForm.css';
import './Draggable.css';
// import '../Designs/index.css';

import left from '../../icons/left.svg';

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
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  // const [input3, setInput3] = useState('');
  // const [input4, setInput4] = useState('');
  // const [input5, setInput5] = useState('');

  const [backgroundColor, setBackgroundColor] = useState('white');

  useEffect(() => {
    dispatch(getAllDesigns());
    dispatch(getAllBrands());
    return () => dispatch(clearData())
  }, [dispatch])

  // DRAG FXNS -------------------------------
  // const dragItem = (item) => {
  //   // console.log('ITEM', item)
  //   let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  //   if (document.getElementById(item)) {
  //     item.onmousedown = dragMouseDown;
  //   }

  //   const dragMouseDown = (e) => {
  //     e = e || window.event;
  //     e.preventDefault();
  //     // grabs mouse position on start
  //     pos3 = e.clientX;
  //     pos4 = e.clientY;

  //     document.onmouseup = closeDragItem;
  //     // this happens when cursor moves
  //     document.onmousemove = itemDrag;
  //   }

  //   const itemDrag = (e) => {
  //     e = e || window.event;
  //     e.preventDefault();

  //     // calculates the item's new position (x, y coords)
  //     pos1 = pos3 - e.clientX;
  //     pos2 = pos4 - e.clientY;
  //     pos3 = e.clientX;
  //     pos4 = e.clientY;
  //     // sets the new position
  //     item.style.top = (item.offsetTop - pos2) + 'px';
  //     item.style.left = (item.offsetLeft - pos1) + 'px';
  //   }

  //   const closeDragItem = () => {
  //     // item stops moving when mouse is released
  //     document.onmouseup = null;
  //     document.onmousemove = null;
  //   }
  // }

  // dragItem(document.getElementById('drag-text'));

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

    if (name.length > 25) errors.push('The name of this design is too long.')
    if (!name.length) errors.push('Please enter a name for the design.')
    setValidationErrs(errors);
  }, [name]);

  const handleSubmit = async e => {
    e.preventDefault();

    setHasSubmit(true);

    const payload = {
      name,
      template: alias,
      text_input_1: input1,
      text_input_2: input2,
      // text_input_3: input3,
      // text_input_4: input4,
      // text_input_5: input5,
    };
    // console.log('CREATE PAYLOAD', payload)
    if (!validationErrs.length) {
      let createdDes = await dispatch(createDesign(payload));
      // console.log('template', alias)
      if (createdDes) history.push(`/designs/${createdDes.id}/${alias}`);
    };
  };

  // LOADING TEMPLATES --------------------------------------------------
  let template;
  // PRESENTATION -----------------------------------
  if (alias === 'presentation-original') {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          backgroundImage: `url(${pres1})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
              width: '880px',
              height: '440px',
              maxWidth: '880px',
              maxHeight:'440px',
              minWidth: '347px',
              minHeight: '120px'
            }}
          />
        </div>
      </div>
    )
  }
  if (alias === 'presentation-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          backgroundImage: `url(${pres2})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
              width: '880px',
              height: '440px',
              maxWidth: '880px',
              maxHeight:'440px',
              minWidth: '347px',
              minHeight: '120px'
            }}
          />
        </div>
      </div>
    )
  }
  if (alias === 'presentation-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          backgroundImage: `url(${pres3})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
              width: '880px',
              height: '440px',
              maxWidth: '880px',
              maxHeight:'440px',
              minWidth: '347px',
              minHeight: '120px'
            }}
          />
        </div>
      </div>
    )
  }
  if (alias === 'presentation-green') {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          backgroundImage: `url(${pres4})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'presentation-bw') {
    template = (
      <div
        className="template"
        style={{
          width: '960px',
          height: '540px',
          backgroundImage: `url(${pres5})`,
          backgroundColor: `${backgroundColor}`
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
              maxHeight:'440px',
              minWidth: '347px',
              minHeight: '120px',
              marginLeft: '120px'
            }}
          />
        </div>
      </div>
    )
  }
  // WEBSITE -----------------------------------
  if (alias === 'website-original') {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          backgroundImage: `url(${web1})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
              maxHeight:'240px',
              minWidth: '347px',
              minHeight: '120px'
            }}
          />
        </div>
      </div>
    )
  }
  if (alias === 'website-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          backgroundImage: `url(${web2})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
              maxHeight:'240px',
              minWidth: '347px',
              minHeight: '120px'
            }}
          />
        </div>
      </div>
    )
  }
  if (alias === 'website-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          backgroundImage: `url(${web3})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
              maxHeight:'240px',
              minWidth: '347px',
              minHeight: '120px'
            }}
          />
        </div>
      </div>
    )
  }
  if (alias === 'website-green') {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          backgroundImage: `url(${web4})`,
          backgroundColor: `${backgroundColor}`
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
              maxHeight:'240px',
              // minWidth: '347px',
              minHeight: '120px',
              marginLeft: '270px'
            }}
          />
        </div>
      </div>
    )
  }
  if (alias === 'website-bw') {
    template = (
      <div
        className="template"
        style={{
          width: '683px',
          height: '384px',
          backgroundImage: `url(${web5})`,
          backgroundColor: `${backgroundColor}`
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
        </div>
      </div>
    )
  }
  // RESUME -----------------------------------
  if (alias === 'resume-original') {
    template = (
      <div
        className="template"
        style={{
          width: '425px',
          height: '550px',
          backgroundImage: `url(${res1})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'resume-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '425px',
          height: '550px',
          backgroundImage: `url(${res2})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'resume-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '425px',
          height: '550px',
          backgroundImage: `url(${res3})`,
          backgroundColor: `${backgroundColor}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'resume-green') {
    template = (
      <div
        className="template"
        style={{
          width: '425px',
          height: '550px',
          backgroundImage: `url(${res4})`,
          backgroundColor: `${backgroundColor}`
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
        </div>
      </div>
    )
  }
  if (alias === 'resume-bw') {
    template = (
      <div
        className="template"
        style={{
          width: '425px',
          height: '550px',
          backgroundImage: `url(${res5})`,
          backgroundColor: `${backgroundColor}`
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
        </div>
      </div>
    )
  }
  // IG POST -----------------------------------
  if (alias === 'igpost-original') {
    template = (
      <div
        className="template"
        style={{
          width: '480px',
          height: '480px',
          backgroundImage: `url(${ig1})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'igpost-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '480px',
          height: '480px',
          backgroundImage: `url(${ig2})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'igpost-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '480px',
          height: '480px',
          backgroundImage: `url(${ig3})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'igpost-green') {
    template = (
      <div
        className="template"
        style={{
          width: '480px',
          height: '480px',
          backgroundImage: `url(${ig4})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'igpost-bw') {
    template = (
      <div
        className="template"
        style={{
          width: '480px',
          height: '480px',
          backgroundImage: `url(${ig5})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  // IG STORY -----------------------------------
  if (alias === 'igstory-original') {
    template = (
      <div
        className="template"
        style={{
          width: '270px',
          height: '480px',
          backgroundImage: `url(${igs1})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'igstory-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '270px',
          height: '480px',
          backgroundImage: `url(${igs2})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'igstory-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '270px',
          height: '480px',
          backgroundImage: `url(${igs3})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'igstory-green') {
    template = (
      <div
        className="template"
        style={{
          width: '270px',
          height: '480px',
          backgroundImage: `url(${igs4})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
              width: '200px',
              marginTop: '40px'
            }}
          />
          {/* <textarea
            id='input2'
            value={input2}
            placeholder="Your text here"
            onChange={(e) => setInput2(e.target.value)}
          /> */}
        </div>
      </div>
    )
  }
  if (alias === 'igstory-pink') {
    template = (
      <div
        className="template"
        style={{
          width: '270px',
          height: '480px',
          backgroundImage: `url(${igs5})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
              width: '200px',
              marginBottom: '40px',
              marginLeft: '24px',
              transform: 'rotate(4deg)'
            }}
          />
          {/* <textarea
            id='input2'
            value={input2}
            placeholder="Your text here"
            onChange={(e) => setInput2(e.target.value)}
          /> */}
        </div>
      </div>
    )
  }
  // FB POST -----------------------------------
  if (alias === 'fbpost-original') {
    template = (
      <div
        className="template"
        style={{
          width: '470px',
          height: '394px',
          backgroundImage: `url(${fb1})`,
          backgroundColor: 'white'
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'fbpost-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '470px',
          height: '394px',
          backgroundImage: `url(${fb2})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'fbpost-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '470px',
          height: '394px',
          backgroundImage: `url(${fb3})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'fbpost-green') {
    template = (
      <div
        className="template"
        style={{
          width: '470px',
          height: '394px',
          backgroundImage: `url(${fb4})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'fbpost-bw') {
    template = (
      <div
        className="template"
        style={{
          width: '470px',
          height: '394px',
          backgroundImage: `url(${fb5})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
              marginBottom: '235px'
            }}
          />
          {/* <textarea
            id='input2'
            value={input2}
            placeholder="Your text here"
            onChange={(e) => setInput2(e.target.value)}
          /> */}
        </div>
      </div>
    )
  }
  // INVITE -----------------------------------
  if (alias === 'invitation-original') {
    template = (
      <div
        className="template"
        style={{
          width: '375px',
          height: '525px',
          backgroundImage: `url(${inv1})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'invitation-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '375px',
          height: '525px',
          backgroundImage: `url(${inv2})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'invitation-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '375px',
          height: '525px',
          backgroundImage: `url(${inv3})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
        }}
      >
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
        </div>
      </div>
    )
  }
  if (alias === 'invitation-green') {
    template = (
      <div
        className="template"
        style={{
          width: '375px',
          height: '525px',
          backgroundImage: `url(${inv4})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'invitation-bw') {
    template = (
      <div
        className="template"
        style={{
          width: '375px',
          height: '525px',
          backgroundImage: `url(${inv5})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  // BIZCARD -----------------------------------
  if (alias === 'businesscard-original') {
    template = (
      <div
        className="template"
        style={{
          width: '336px',
          height: '192px',
          backgroundImage: `url(${biz1})`,
          backgroundSize: 'contain',
          backgroundRepeat: 'no-repeat',
          backgroundPositionX: 'center',
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'businesscard-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '336px',
          height: '192px',
          backgroundImage: `url(${biz2})`,
          backgroundSize: 'contain',
          backgroundRepeat: 'no-repeat',
          backgroundPositionX: 'center',
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'businesscard-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '336px',
          height: '192px',
          backgroundImage: `url(${biz3})`,
          backgroundSize: 'contain',
          backgroundRepeat: 'no-repeat',
          backgroundPositionX: 'center',
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'businesscard-green') {
    template = (
      <div
        className="template"
        style={{
          width: '336px',
          height: '192px',
          backgroundImage: `url(${biz4})`,
          backgroundSize: 'contain',
          backgroundRepeat: 'no-repeat',
          backgroundPositionX: 'center',
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  if (alias === 'businesscard-bw') {
    template = (
      <div
        className="template"
        style={{
          width: '336px',
          height: '192px',
          backgroundImage: `url(${biz5})`,
          backgroundSize: 'contain',
          backgroundRepeat: 'no-repeat',
          backgroundPositionX: 'center',
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
        </div>
      </div>
    )
  }
  // INFOGRAPH -------------------------
  if (alias === 'infograph-original') {
    template = (
      <div
        className="template"
        style={{
          width: '200px',
          height: '500px',
          backgroundImage: `url(${info1})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
              width: '150px',

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
  if (alias === 'infograph-fun') {
    template = (
      <div
        className="template"
        style={{
          width: '200px',
          height: '500px',
          backgroundImage: `url(${info2})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
  if (alias === 'infograph-aesthetic') {
    template = (
      <div
        className="template"
        style={{
          width: '200px',
          height: '500px',
          backgroundImage: `url(${info3})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
  if (alias === 'infograph-green') {
    template = (
      <div
        className="template"
        style={{
          width: '200px',
          height: '500px',
          backgroundImage: `url(${info4})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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
  if (alias === 'infograph-bw') {
    template = (
      <div
        className="template"
        style={{
          width: '200px',
          height: '500px',
          backgroundImage: `url(${info5})`,
          backgroundColor: `${localStorage.getItem('backgroundColor')}`
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

  return (
    <div className="create-des-container">

      <form className='create-des-form' onSubmit={handleSubmit}>
        <div id='home-button' onClick={() => history.push('/designs')}>
          <img src={left} alt='left' height='14px' />
          Home
        </div>
        <div className="form-inputs">
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
            placeholder="Design title"
            value={name}
            onChange={e => setName(e.target.value)}
          />
          <div id='hidden-inputs'>
            <input
              type='text'
              value={alias}
              // hidden
              onChange={e => {
                setTemp(e.target.value)
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
          </div>
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
            <div id='temp-menu-item-brand'>
              <div id='brand-side-content'>Oops! Looks like this feature is still in the works. In the meantime, try checking out brands for the future!

                <button
                  onClick={() => history.push('/brand')}
                >Go to brands</button>
              </div>
            </div>
            // <div id='temp-menu-item'>
            //   {Object.values(brands).map(brand => (
            //     <div className="des-brand-colors">
            //       {brand.colors.map(color => (
            //       <div
            //         onClick={() => {
            //           setBackgroundColor(color.name);
            //           localStorage.setItem('backgroundColor', color.name)
            //         }}
            //       >{color.name}</div>
            //       ))}
            //       {brand.fonts.map(font => (
            //         <div>
            //           {font.name}
            //         </div>
            //       ))}
            //     </div>
            //   ))}
            // </div>
          )}
          {/* <button onClick={openSideMenu}>Text</button>
        <button onClick={openSideMenu}>Styles</button>
        <button onClick={openSideMenu}>Logos</button> */}
        </div>

        <div className="edit-area">
          {/* <div id='under-construction'>This feature is in the making</div> */}
          <div id="inserted-temp">{template}</div>
          {/* <div
            id='drag-text'

            height='100px'
            width='100px'
            // draggable
          >
          hi
          </div> */}
        </div>
      </div>
    </div>
  )

}
