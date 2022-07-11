import React, {useEffect} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {Row, Col, Card, Table} from 'react-bootstrap'
import Loader from '../components/Loader'
import Message from '../components/Message'
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer} from 'recharts'
import {listOrders} from "../actions/orderActions"

function HomeScreen({history}) {
    const dispatch = useDispatch()
    const orderList = useSelector(state => state.orderList)
    const {error, loading, orders} = orderList
    let total_cost_usd = 0
    let total_cost_rub = 0
    for (let i = 0; i < orders.length; i += 1) {
        const order = orders[i]
        total_cost_usd += order.cost_in_usd
        total_cost_rub += order.cost_in_rub
    }
    useEffect(() => {
        dispatch(listOrders())
        setInterval(() => {
            dispatch(listOrders())
        }, 30000);
    }, [dispatch])
    const data = orders;

    return (
        <div>
            <h1>Заказы</h1>
            {loading ? <Loader/>
                : error ? <Message variant='danger'>{error}</Message>
                    :
                    <Row>
                        <Col>
                            <ResponsiveContainer width="95%" height="50%">
                                <LineChart
                                    width={600}
                                    height={300}
                                    data={data}
                                    margin={{
                                        top: 5,
                                        right: 0,
                                        left: 20,
                                        bottom: 5,
                                    }}>
                                    <CartesianGrid strokeDasharray="3 3"/>
                                    <XAxis dataKey="delivery_date" height={0}/>
                                    <YAxis/>
                                    <Tooltip/>
                                    <Legend/>
                                    <Line type="monotone" name="Стоимость в долларах" dataKey="cost_in_usd"
                                          stroke="#8884d8"
                                          activeDot={{r: 9}}/>
                                </LineChart>
                            </ResponsiveContainer>
                            <ResponsiveContainer width="95%" height="50%">
                                <LineChart
                                    width={600}
                                    height={300}
                                    data={data}
                                    margin={{
                                        top: 5,
                                        right: 0,
                                        left: 20,
                                        bottom: 5,
                                    }}>
                                    <CartesianGrid strokeDasharray="3 3"/>
                                    <XAxis dataKey="delivery_date" height={0}/>
                                    <YAxis/>
                                    <Tooltip/>
                                    <Legend/>
                                    <Line type="monotone" name="Стоимость в рублях" dataKey="cost_in_rub"
                                          stroke="#8884d8"
                                          activeDot={{r: 9}}/>
                                </LineChart>
                            </ResponsiveContainer>
                        </Col>
                        <Col>
                            <Card className='my-3 p-3 rounded'>
                                <Card.Body>
                                    <Card.Title>Всего</Card.Title>
                                    <Card.Text>
                                        В долларах: {total_cost_usd}
                                    </Card.Text>
                                    <Card.Text>
                                        В рублях: {total_cost_rub}
                                    </Card.Text>
                                </Card.Body>
                            </Card>
                            <div className='my-custom-scrollbar table-wrapper-scroll-y'>
                                <Table striped bordered hover size="sm" className='table-sm p-3'>
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Номер заказа</th>
                                            <th>Дата доставки</th>
                                            <th>$</th>
                                            <th>руб</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {orders.map(order => (
                                            <tr>
                                                <td>{order.number}</td>
                                                <td>{order.order_number}</td>
                                                <td>{order.delivery_date}</td>
                                                <td>{order.cost_in_usd}</td>
                                                <td>{order.cost_in_rub}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </Table>
                            </div>
                        </Col>
                    </Row>
            }
        </div>
    )
}

export default HomeScreen