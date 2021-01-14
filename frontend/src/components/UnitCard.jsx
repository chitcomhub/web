import React from 'react';

import { getTelegramLink, getGithubLink } from '../util/stuff';

import defaultProfileImg from './../assets/images/default-profile.png';
import socialGithub from './../assets/images/social/github.png';
import socialTelegram from './../assets/images/social/telegram.png';

const UnitCard = (props) => {
  const unit = props.unit;
  return (
    <div className="col-md-4 col-lg-3 col-sm-10 col-11 user-card">
      <div className="block-user">
        <img src={defaultProfileImg} className="img-user" />
        <div>
          <h5>
            {unit.first_name} {unit.last_name}
          </h5>
          <p>{unit.short_bio}</p>
          <span>Python</span>
          <span>Android</span>
        </div>
      </div>
      <div className="block-socials">
        <a href={getGithubLink(unit.github)}>
          <img src={socialGithub} className="icon-social" />
        </a>
        <a href={getTelegramLink(unit.telegram)}>
          <img src={socialTelegram} className="icon-social" />
        </a>
      </div>
    </div>
  );
};

export default UnitCard;
