from subjugate.template.engine import GenericEngine
from subjugate.template import SubjugateTemplate

class SubjugateTemplates(GenericEngine):
    template_cls = SubjugateTemplate
    app_dirname = "subjugate"

    def __init__(self, params):
        params = params.copy()
        self.dirs = list(params.pop('DIRS')) or []
        self.app_dirs = bool(params.pop('APP_DIRS'))
        options = params.pop('OPTIONS')

        super().__init__(self.dirs, self.app_dirs, **options)
