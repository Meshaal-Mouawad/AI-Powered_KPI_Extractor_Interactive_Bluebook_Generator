Benzene Purity %
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_01.tsql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_01.tsql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Benzene%20Purity%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Benzene Purity % measures the concentration of benzene in a given sample</li><li>expressed as a percentage</li><li>This KPI is crucial for assessing the quality of benzene produced in petrochemical processes</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of monitoring Benzene Purity % is to ensure that the benzene produced meets industry standards and specifications</li><li>thereby maintaining product quality and safety</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The Benzene Purity % is derived from the measurement of benzene concentration in a sample, represented as a percentage of the total volume.</p>
               <p>See code context for implementation details.</p>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               0.0s (AI 0.0s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 0.001s
                  • AI: 0.001s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>88.9%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>11.1%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>Benzene Purity % is utilized in various KPIs related to product quality</li><li>process efficiency</li><li>and compliance with regulatory standards in the petrochemical industry</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measure for calculating Benzene Purity % is the volume of benzene present in the sample compared to the total volume of the sample</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Benzene Purity % is percentage (%).</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The reporting source for Benzene Purity % is typically derived from laboratory analysis and quality control assessments conducted during the production process.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Maintaining high Benzene Purity % is essential for meeting customer requirements and regulatory compliance, as impurities can affect the performance and safety of benzene in various applications.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Benzene Purity %
   WITH s AS (
     SELECT CAST(99.2 AS DECIMAL(5,2)) AS purity
   )
   SELECT purity AS [Benzene Purity %]
   FROM s;