import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import { createDesign } from "../../store/designs";

import './CreateDesignForm.css';

export default function CreateDesign() {
  const dispatch = useDispatch();
  const history = useHistory();
  const url = useLocation().pathname;
  // console.log('CURRENT URL: ', url)
  const user = useSelector(state => state.session.user);

  let alias = url.split('/')[3]
  // console.log('Alias', alias)
  const [name, setName] = useState('');
  const [template, setTemplate] = useState('');
  const [validationErrs, setValidationErrs] = useState([]);
  const [hasSubmit, setHasSubmit] = useState(false);

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

  return (
    <div>
      <div className="sidebar">
        <button>Templates</button>
        <button>Elements</button>
        <button>Text</button>
        <button>Styles</button>
        <button>Logos</button>
      </div>
      <form onSubmit={handleSubmit}>
      Create Design Form HERE
        <input
          type='text'
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <button type='submit'>Save new design</button>
      </form>
      <div className="edit-area">
        <div id="inserted-temp"></div>
      </div>
    </div>
  )

}
