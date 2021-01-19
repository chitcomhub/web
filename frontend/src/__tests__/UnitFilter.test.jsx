import React from 'react';
import { render, unmountComponentAtNode } from 'react-dom';
import { act } from 'react-dom/test-utils';
import UnitFilter from '../components/UnitFilter';
import * as api from '../util/api';

// ------ prepare stuff ----------
let container = null;
beforeEach(() => {
  // setup a DOM element as a render target
  container = document.createElement('div');
  document.body.appendChild(container);
});

afterEach(() => {
  // cleanup on exiting
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});

// --------- testing -------------

// test 1
it('Renders unit data simple case', async () => {
  const fakeUnit = {
    id: 1,
    first_name: 'Iункурбек',
    last_name: 'Султанов',
    short_bio: 'Сеньор разработчик из Грозный-Сити',
    telegram: 'arbios',
    github: 'arbios',
  };

  // mock api func
  api.getAllUnits = jest.fn().mockReturnValue([fakeUnit]);

  await act(async () => {
    render(<UnitFilter />, container);
  });

  // check the name and bio
  let userMainInfoBlock = document.querySelector('.user-card .block-user div');
  expect(userMainInfoBlock.querySelector('h5').textContent).toBe(
    fakeUnit.first_name + ' ' + fakeUnit.last_name,
  );
  expect(userMainInfoBlock.querySelector('p').textContent).toBe(fakeUnit.short_bio);

  // check social urls present and correct
  let socialLinks = document.querySelector('.user-card .block-socials').querySelectorAll('a');
  const urls = Array.from(
    document.querySelector('.user-card .block-socials').querySelectorAll('a'),
  ).map((a) => a.href);
  expect(urls.sort()).toEqual(
    ['https://t.me/' + fakeUnit.telegram, 'https://github.com/' + fakeUnit.github].sort(),
  );
  // remove the mock
  api.getAllUnits.mockRestore();
});
