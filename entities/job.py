from entities.technology import Technology


class Job:
    def __init__(self, the_id=None, unique_id=None, enterprise_name=None, skills=None, languages=None, name=None,
                 date=None,
                 address=None,
                 contract_type=None, qualification=None, technology=None, title=None):
        if the_id is not None and unique_id is not None and enterprise_name is not None and skills is not None and languages is not None and name is not None and date is not None and address is not None and contract_type is not None and qualification is not None and technology is not None and title is not None:
            self._id = the_id
            self._unique_id = unique_id
            self._experience = enterprise_name
            self._skills = skills
            self._languages = languages
            self._enterprise_name = name
            self._date = date
            self._address = address
            self._contract_type = contract_type
            self._qualification = qualification
            self._technology = technology
            self._title = title
        else:
            self._id = ''
            self._unique_id = ''
            self._experience = ''
            self._skills = ''
            self._languages = ''
            self._enterprise_name = ''
            self._date = ''
            self._address = ''
            self._contract_type = ''
            self._qualification = ''
            self._technology = Technology()
            self._title = ''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, value):
        self._skills = value

    @property
    def languages(self):
        return self._languages

    @languages.setter
    def languages(self, value):
        self._languages = value

    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def contract_type(self):
        return self._contract_type

    @contract_type.setter
    def contract_type(self, value):
        self._contract_type = value

    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, value):
        self._qualification = value

    @property
    def technology(self):
        return self._technology

    @technology.setter
    def technology(self, value):
        self._technology = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def __str__(self):
        return f"Job(id={self.id},technology_id={self.technology.id},enterprise_name={self.enterprise_name},skills=[{self.skills}],date={self.date},address={self.address},contract_type={self.contract_type},qualification={self.qualification},experience={self.experience},language={self.languages},title={self._title}\n"
