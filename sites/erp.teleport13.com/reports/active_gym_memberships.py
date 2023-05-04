import frappe

from frappe import _
from frappe.utils import today
from frappe.query_report import generate_report_result

def execute(filters=None):
    columns = [
        {"label": _("Member Name"), "fieldname": "full_name", "fieldtype": "Link", "options": "Gym Subscription Member", "width": 150},
        {"label": _("Plan Type"), "fieldname": "plan_type", "width": 150},
        {"label": _("Start Date"), "fieldname": "start_date", "fieldtype": "Date", "width": 120},
        {"label": _("End Date"), "fieldname": "end_date", "fieldtype": "Date", "width": 120},
    ]

    data = get_data(filters)

    return columns, data

def get_data(filters=None):
    conditions = f"end_date >= '{today()}'"

    data = frappe.db.sql(
        f"""
        SELECT 
            `member`.`name` as member_name,
            `membership`.`plan_type` as plan_type,
            `membership`.`start_date` as start_date,
            `membership`.`end_date` as end_date
        FROM 
            `tabGym Membership` as `membership`
        JOIN 
            `tabGym Member` as `member`
        ON 
            `membership`.`member` = `member`.`name`
        WHERE 
            {conditions}
        """
    )

    return data
