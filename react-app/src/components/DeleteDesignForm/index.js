import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { deleteDesign } from "../../store/designs";

export default function DeleteDesign() {
  const design = useSelector(state => state.designs.singleDesign);
  const dispatch = useDispatch();
  const history = useHistory();

  const handleDelete = async e => {
    e.preventDefault();

    const deletion = dispatch(deleteDesign(design.id));
    if (deletion) history.push('/');
  };

  return (
    <button id='create-des-button' onClick={handleDelete}>Remove design</button>
  )
};
