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
    l.owneroccupied;