{
    "name": "Gestion des étudiants",
    "version": "1.0",
    "category": "Generic Modules/Others",
    "description": """Test création module gestion des étudiants Odoo v14""",
    "author": "chamoley",
    "depends": ["base"],
    "data": [
        "data/students_student_data.xml",
        "data/students_training_data.xml",
        "data/students_mark_data.xml",

        "views/students_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
