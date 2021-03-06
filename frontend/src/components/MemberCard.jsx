import React from 'react';

import { getTelegramLink, getGithubLink } from '../util/stuff';

import defaultProfileImg from './../assets/images/default-profile.png';
import socialGithub from './../assets/images/social/github.png';
import socialTelegram from './../assets/images/social/telegram.png';

const MemberCard = (props) => {
  const member = props.member;
  return (
    <div className="col-md-4 col-lg-3 col-sm-10 col-11 user-card">
      <div className="block-user">
        <img src={defaultProfileImg} className="img-user" alt="Member avatar"/>
        <div>
          <h5>
            {member.first_name} {member.last_name}
          </h5>
          <p>{member.short_bio}</p>
          <span>Python</span>
          <span>Android</span>
        </div>
      </div>
      <div className="block-socials">
        <a href={getGithubLink(member.github)}>
          <img src={socialGithub} className="icon-social" alt="Github"/>
        </a>
        <a href={getTelegramLink(member.telegram)}>
          <img src={socialTelegram} className="icon-social" alt="Telegram"/>
        </a>
      </div>
    </div>
  );
};

export default MemberCard;
