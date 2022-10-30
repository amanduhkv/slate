import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { createDesign } from "../../store/designs";

export default function CreateDesign() {
  const dispatch = useDispatch();
  const history = useHistory();

  const user = useSelector(state => state.session.user);

  const [name, setName] = useState('');
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
      name
    };

    if (!validationErrs.length) {
      let createdDes = await dispatch(createDesign(payload));

      if (createdDes) history.push(`/designs/${createdDes.id}`);
    };
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
      Create Design Form HERE
        <input
          type='text'
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <button type='submit'>Create new design</button>
      </form>
    </div>
  )

}
