import React from 'react';
import styles from 'styles';

export const TheForm = styles.form`
    margin-top: 20px;
    width: 800px;
    margin-left: auto;
    margin-right: auto;
`;

export const FormGroup = styles.div`
    background-color: rgb(180, 179, 179);
    border-radius: 10px;
    width: 450px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    padding-top: 10px;
    padding-bottom: 10px;
`;
export const FillLabel = styles.label`
    display: inline-block;
    width: 160px;
    text-align: left;
    color: white;
    margin-right: 20px;
    font-size: 20px;
`;
export const MainInput = styles.input`
    width: 230px;
    border: none;
    height: 30px;
    color: rgb(179, 34, 236);
    font-weight: 600;
    border-radius: 0px 5px 5px 0px;
`;
export const RoundedBtn = styles.button`
    color: white;
    background-color: #8520E9;
    border-radius: 15px;
    height: 30px;
    width: 150px;
    border: none;
    margin-top: 20px;
    font-size: 20px;
    font-weight: bold;
`;
export const Danger = styles.p`
    color: red;
`;