truncate_query = """
    TRUNCATE TABLE rental_payments_opa_mvw
"""

eclipse_extract = """
    SELECT
        l.licensenumber,
        p.opafulladdress opaaddress,
        p.opaaccountnumber,
        l.numberofunits,
        l.owneroccupied,
        SUM(fee.paymenttotal) totalfeepayments
    FROM
        query.o_fn_fee fee,
        api.jobs job,
        lmscorral.bl_joblicensexref jl,
        lmscorral.bl_license l,
        lmscorral.bl_business b,
        lmscorral.address a,
        lmscorral.parcel p
    WHERE
        l.objectid = jl.licenseobjectid
        AND jl.jobid = job.jobid
        AND job.jobid = fee.referencedobjectid
        AND b.addressobjectid = a.objectid
        AND b.parcelobjectid = p.objectid
        AND l.businessobjectid = b.objectid
        AND job.statusid LIKE '1036493'
        AND l.mostrecentissuedate BETWEEN ( job.completeddate - 2 ) AND ( job.completeddate + 2 )
    GROUP BY
        l.licensenumber,
        p.opaaccountnumber,
        p.opafulladdress,
        l.numberofunits,
        l.owneroccupied
"""

gislni_insert = """
    INSERT INTO rental_payments_opa_mvw (
        licensenumber,
        opaaddress,
        opaaccountnumber,
        numberofunits,
        owneroccupied,
        totalfeepayments
    ) VALUES (
        :1,
        :2,
        :3,
        :4,
        :5,
        :6
    )
"""

# exporting queries
class SqlQuery:
    def __init__(self, extract_query, load_query):
        self.extract_query = extract_query
        self.load_query = load_query

# create instances for SqlQuery class
eclipse_to_gislni_query = SqlQuery(eclipse_extract, gislni_insert)