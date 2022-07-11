import axios from 'axios'
import {

    ORDER_LIST_REQUEST,
    ORDER_LIST_SUCCESS,
    ORDER_LIST_FAIL,

} from '../constants/orderConstants'


export const listOrders = () => async (dispatch) => {
    try {
        dispatch({ type: ORDER_LIST_REQUEST })

        const { data } = await axios.get(`/api/orders`)

        dispatch({
            type: ORDER_LIST_SUCCESS,
            payload: data
        })

    } catch (error) {
        dispatch({
            type: ORDER_LIST_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}