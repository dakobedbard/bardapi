import { combineReducers } from "redux";
import visibilityFilter from "./visibilityFilter";
import todos from "../reducers/todos";

export default combineReducers({ todos, visibilityFilter });
