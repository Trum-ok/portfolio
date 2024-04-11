import React from 'react';
import { FormEvent, useState } from 'react';

interface ILoginForm {
  username: string;
  password: string;
}

const AdminInputForm: React.FC = () => {
  const [formData, setFormData] = useState<ILoginForm>({
    username: '',
    password: ''
  });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value
    });
  };

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    // на сервер
    console.log('Login data:', formData);
  };

  return (
    <div className="adminInputForm">
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Логин</label>
        <input
          type="text"
          name="username"
          id="username"
          value={formData.username}
          onChange={handleChange}
        />
        <label htmlFor="password">Пароль</label>
        <input
          type="password"
          name="password"
          id="password"
          value={formData.password}
          onChange={handleChange}
        />
        <button type="submit">Войти</button>
      </form>
    </div>
  );
};

export default AdminInputForm;