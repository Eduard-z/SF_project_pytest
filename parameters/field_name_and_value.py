# create object and define properties for a field: name and value
class AccountNameFieldNameValue:
    def __init__(self, name="Account Name", value="A1"):
        self.name = name
        self.value = value


class ProspectRatingFieldNameValue:
    def __init__(self, name="Prospect Rating", value="Warm"):
        self.name = name
        self.value = value


class SupportPlanExpirationDateFieldNameValue:
    def __init__(self, name="Support Plan Expiration Date", value="05/02/2002"):
        self.name = name
        self.value = value


HasSupportPlan = ('Has Support Plan', 'checked')
