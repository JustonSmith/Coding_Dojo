import React from 'react';
import useForm from './useForm';
import userValidation from './UserValidation';
import { TheForm, FillLabel, FormGroup, MainInput, Danger, RoundedBtn} from './styles';

const MainForm = () => {
    const login = () => {
        console.log("no errors. Submit callback.")
    };
    const {
        values,
        errors, 
        handleChange,
        handleSubmit,
    } = useForm(login, userValidation);
    return (
        <div>
            <h2>Make an Account</h2>
            <TheForm>
                <FormGroup>
                    <FillLabel>First Name: {" "}</FillLabel>
                    <MainInput className={`input ${errors.firstName && 'is-danger'}`} type="firstName" name="firstName" onChange={handleChange} value= {values.firstName || ''} required />
                </FormGroup>
                <FormGroup>
                    <FillLabel>Last Name: {" "}</FillLabel>
                    <MainInput className={`input ${errors.lastName && 'is-danger'}`} type="lastName" name="lastName" onChange={handleChange} value= {values.lastName || ''} required />
                </FormGroup>
                <FormGroup>
                    <FillLabel>Email: {" "}</FillLabel>
                    <MainInput autoComplete="off" className={`input ${errors.Email && 'is-danger'}`} type="email" name="email" onChange={handleChange} value= {values.email || ''} required />
                </FormGroup>
                <FormGroup>
                    <FillLabel>Password: {" "}</FillLabel>
                    <MainInput className={`input ${errors.password && 'is-danger'}`} type="password" name="password" onChange={handleChange} value= {values.password || ''} required />
                </FormGroup>
                <FormGroup>
                    <FillLabel>Confirm Password: {" "}</FillLabel>
                    <MainInput className={`input ${errors.confirmPassword && 'is-danger'}`} type="confirmPassword" name="confirmPassword" onChange={handleChange} value= {values.confirmPassword || ''} required />
                </FormGroup>
                <RoundedBtn type= "submit"> Register</RoundedBtn>

                {errors.firstName && (<Danger>{errors.firstName}</Danger>)}
                {errors.lastName && (<Danger>{errors.lastName}</Danger>)}
                {errors.email && (<Danger>{errors.email}</Danger>)}
                {errors.password && (<Danger>{errors.password}</Danger>)}
                {errors.confirmPassword && (<Danger>{errors.confirmPassword}</Danger>)}
            </TheForm>
        </div>
    )
}
export default MainForm;