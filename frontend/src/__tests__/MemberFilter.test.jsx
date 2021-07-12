import React from 'react';
import { render, unmountComponentAtNode } from 'react-dom';
import { act } from 'react-dom/test-utils';
import MemberFilter from '../components/MemberFilter';
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
it('Renders member data simple case', async () => {
  const fakeMember = {
    id: 1,
    first_name: 'Iункурбек',
    last_name: 'Султанов',
    short_bio: 'Сеньор разработчик из Грозный-Сити',
    telegram: 'arbios',
    github: 'arbios',
  };

  // mock api func
  api.getAllMembers = jest.fn().mockReturnValue([fakeMember]);

  await act(async () => {
    render(<MemberFilter />, container);
  });

  // check the name and bio
  let userMainInfoBlock = document.querySelector('.user-card .block-user div');
  expect(userMainInfoBlock.querySelector('h5').textContent).toBe(
    fakeMember.first_name + ' ' + fakeMember.last_name,
  );
  expect(userMainInfoBlock.querySelector('p').textContent).toBe(fakeMember.short_bio);

  // check social urls present and correct
  let socialLinks = document.querySelector('.user-card .block-socials').querySelectorAll('a');
  const urls = Array.from(
    document.querySelector('.user-card .block-socials').querySelectorAll('a'),
  ).map((a) => a.href);
  expect(urls.sort()).toEqual(
    ['https://t.me/' + fakeMember.telegram, 'https://github.com/' + fakeMember.github].sort(),
  );
  // remove the mock
  api.getAllMembers.mockRestore();
});
